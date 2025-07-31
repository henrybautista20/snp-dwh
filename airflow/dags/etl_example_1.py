from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='etl_example_1',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['spark'],
) as dag:

    run_spark = SparkSubmitOperator(
        task_id='run_remote_spark_job',
        application='/opt/airflow/spark_jobs/example_1.py',  
        conn_id='spark_remote',
        verbose=True
    )
    
