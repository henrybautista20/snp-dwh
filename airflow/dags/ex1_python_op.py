from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def my_python_task():
    print("Hola desde PythonOperator!")

with DAG('example_python_operator',
         start_date=datetime(2025, 8, 5),
         schedule_interval=None,
         catchup=False) as dag:

    task_python = PythonOperator(
        task_id='run_python_function',
        python_callable=my_python_task
    )