from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('example_bash_operator',
         start_date=datetime(2025, 8, 5),
         schedule_interval=None,
         catchup=False) as dag:

    task_bash = BashOperator(
        task_id='print_date',
        bash_command='echo "La fecha actual es: $(date)"'
    )
