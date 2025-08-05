from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime
from hadoop_sensor import HadoopFileSensor   # <- importar tu clase personalizada

jars = [
    "/opt/airflow/spark_jobs/jars/spark-excel_2.12-0.13.7.jar",
    "/opt/airflow/spark_jobs/jars/poi-4.1.2.jar",
    "/opt/airflow/spark_jobs/jars/poi-ooxml-4.1.2.jar",
    "/opt/airflow/spark_jobs/jars/xmlbeans-3.1.0.jar",
    "/opt/airflow/spark_jobs/jars/commons-math3-3.6.1.jar",
    "/opt/airflow/spark_jobs/jars/ooxml-schemas-1.4.jar",
    "/opt/airflow/spark_jobs/jars/postgresql-42.7.3.jar"
]
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 6, 24),
    'retries': 1,
}

with DAG(
    dag_id='etl_sftp_hadoop_spark_db3',
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
        bash_command='docker exec snp-dwh-hadoop-namenode-1 hdfs dfs -put -f /sftp-data/datos_pnd2425-13-05-2025_n.xlsx /data/',
    )

    wait_for_hdfs_excel = HadoopFileSensor(
        task_id='wait_for_excel_hdfs',
        container_name='snp-dwh-hadoop-namenode-1',
        hdfs_path='/data/datos_pnd2425-13-05-2025_n.xlsx',
        poke_interval=60,   # revisa cada 60s
        timeout=1800        # falla después de 30 minutos
    )

    run_spark = SparkSubmitOperator(
        task_id='run_remote_spark_job',
          application='/opt/airflow/spark_jobs/sftp_hadoop_spark_db.py',
    conn_id='spark_remote',
    conf={
            "spark.driver.memory": "4g",
            "spark.executor.memory": "4g",
            "spark.executor.cores": "2",
            "spark.default.parallelism": "100",
        },
        verbose=True, 
   jars=",".join(jars)
    )
    create_hdfs_folder >> upload_csv_to_hdfs >> wait_for_hdfs_excel >> run_spark