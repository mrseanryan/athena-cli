sql_script_dir=$1
json_out_dir=$2
AWS_REGION=$3
AWS_WORKGROUP=$4
AWS_S3_OUT_PATH=$5

for file in $sql_script_dir/*.sql
do
    ./get_data_from_athena_one_sql_script.sh $file $json_out_dir $AWS_REGION $AWS_WORKGROUP $AWS_S3_OUT_PATH
done

echo "[done]"
