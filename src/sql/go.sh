function get_data_for_dir() {
    SQL_SCRIPTS=$1
    DATA_OUT=$2
    ./get_data_from_athena_via_sql_scripts.sh "$SQL_SCRIPTS" "$DATA_OUT" "$AWS_REGION" "$AWS_WORKGROUP" "$AWS_S3_OUT_PATH"
    ls -al $DATA_OUT
}

echo " === Dashboard 1 ==="
get_data_for_dir ./dashboard-1  ../../data/dashboard-1

echo " === Dashboard 2 ==="
get_data_for_dir ./dashboard-2  ../../data/dashboard-2

echo " === Dashboard 3 ==="
get_data_for_dir ./dashboard-3  ../../data/dashboard-3
