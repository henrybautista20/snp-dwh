from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 6, 24),
    'retries': 1,
}

with DAG(
    dag_id='upload_usuarios_to_hdfs',
    default_args=default_args,
    schedule_interval=None,  # Manual o lo puedes poner diario, '0 6 * * *'
    catchup=False,
    description='Copia usuarios.csv desde /sftp-data en el contenedor hadoop-namenode a HDFS /data',
) as dag:

    create_hdfs_folder = BashOperator(
        task_id='create_hdfs_folder',
        bash_command='docker exec snp-dwh-hadoop-namenode-1 hdfs dfs -mkdir -p /data',
    )

    upload_csv_to_hdfs = BashOperator(
        task_id='upload_csv_to_hdfs',
        bash_command='docker exec snp-dwh-hadoop-namenode-1 hdfs dfs -put -f /sftp-data/usuarios.csv /data/',
    )

    create_hdfs_folder >> upload_csv_to_hdfs
