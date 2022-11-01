# USAGE:
# ./go-one-script.sh   <SQL FILE> <OUTPUT DIR>
#
# EXAMPLE:
# ./go-one-script.sh   ./dashboard-1/clicks-count-per-month.sql   ../../data/dashboard-1

SQL_SCRIPT=$1
DATA_OUT=$2
./get_data_from_athena_one_sql_script.sh "$SQL_SCRIPT" "$DATA_OUT" "$AWS_REGION" "$AWS_WORKGROUP" "$AWS_S3_OUT_PATH"
ls -al $DATA_OUT
