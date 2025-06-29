from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 6, 24),
    'retries': 1,
}

with DAG(
    dag_id='load_csv_to_hdfs',
    default_args=default_args,
    schedule_interval=None,  # Puedes cambiar a '0 6 * * *' para ejecución diaria
    catchup=False,
    description='Copia un archivo CSV desde local a HDFS',
) as dag:

    move_to_hdfs = BashOperator(
        task_id='move_csv_to_hdfs',
        bash_command='/var/snp-dwh/spark_jobs/scripts/load_hadoop.sh',
    )

    move_to_hdfs
