from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

with DAG(
    dag_id='run_pyspark_in_cluster',
    start_date=datetime(2025, 6, 29),
    schedule_interval=None,
    catchup=False,
) as dag:

    spark_job = SparkSubmitOperator(
        task_id='submit_spark_job',  
        application='/opt/spark-apps/mi_script.py',  # ruta en Spark master / workers
        conn_id='spark_remote',  # configurado con spark://snp-dwh-spark-master-1:7077
        application_args=[],
        verbose=True
    )
