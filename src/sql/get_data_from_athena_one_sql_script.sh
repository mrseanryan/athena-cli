sql_file=$1
out_dir=$2
AWS_REGION=$3
AWS_WORKGROUP=$4
AWS_S3_OUT_PATH=$5

echo "Using SQL from $sql_file"
SQL=`cat $sql_file | grep -v '\-\-' | tr '\n' ' '` # Remove commented-out lines. Replace endlines with space, so is all on 1 line.

echo "Execute SQL against Athena:"
echo "$SQL"
QE_ID=`aws athena start-query-execution --query-string "$SQL" --result-configuration "OutputLocation=$AWS_S3_OUT_PATH"  --work-group $AWS_WORKGROUP --region $AWS_REGION --output json | jq -r ".QueryExecutionId"`

echo QE_ID = $QE_ID

OUT_LOC=/tmp/athena.bash.result.json
ERR_LOC=/tmp/athena.bash.error.json

echo "Wait for query to complete..."

IS_RETRYING=1
while [ $IS_RETRYING -gt 0 ] ; do
    sleep 1
    echo "try to get results..."

    aws athena get-query-results --query-execution-id $QE_ID 2>$ERR_LOC 1>$OUT_LOC
    if grep -q "$Current state: FAILED" $ERR_LOC; then
        echo "[SQL FAILED]"
        exit 1
    fi
    if grep -q "$Current state: RUNNING" $ERR_LOC; then
        echo "[SQL RUNNING] Retrying..."
        continue #loop around
    else
        echo "[SQL DONE] Have data."
        IS_RETRYING=0
    fi
done

OUT_LOC_2=$OUT_LOC.2.json

echo "Data at $OUT_LOC"
cat $OUT_LOC | jq  "{ data: [ .ResultSet.Rows[].Data | [ .[].VarCharValue ] | { values: . } ]}" > $OUT_LOC_2

# NOT deleting the file from S3, since permission denied.

# Output to a file named after the SQL script
filename=$(basename -- "$sql_file")
extension="${filename##*.}"
filename="${filename%.*}"

OUT_LOC_3=$out_dir/$filename.json

# Use jq to project from the values based structure of Athena -> compact JSON form that the charts Python scripts can consume.
# This is the same format output by DBeaver
cat $OUT_LOC_2 | jq ".data[0].values as \$header | .data |= (.[1:] | map(.values | with_entries(.key |= \$header[.])))" > $OUT_LOC_3

# cat $OUT_LOC_3

echo "\n\n"
echo $OUT_LOC_3
