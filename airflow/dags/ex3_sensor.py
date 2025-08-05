from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

with DAG('example_file_sensor',
         start_date=datetime(2025, 8, 5),
         schedule_interval=None,
         catchup=False) as dag:

    wait_for_file = FileSensor(
        task_id='wait_for_input_file',
        filepath='/opt/airflow/dags/usuarios.csv',
        poke_interval=30,    # revisa cada 30 segundos
        timeout=600          # tiempo máximo de espera: 10 minutos
    )