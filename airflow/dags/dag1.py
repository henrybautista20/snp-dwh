from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('test_dag_minimo', start_date=datetime(2024,1,1), schedule_interval=None) as dag:
    t = BashOperator(task_id='hola', bash_command='echo hi')
