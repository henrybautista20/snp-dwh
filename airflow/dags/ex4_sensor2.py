from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    'wait_two_jobs_then_third',
    start_date=datetime(2025, 8, 5),
    schedule_interval=None,
    catchup=False,
    description="Espera que dos archivos existan antes de ejecutar una tercera tarea",
) as dag:

    # ✅ Job 1: Espera por el primer archivo
    wait_for_file_1 = FileSensor(
        task_id='wait_for_file_1',
        filepath='/opt/airflow/dags/input1.csv',
        poke_interval=30,
        timeout=600
    )

    # ✅ Job 2: Espera por el segundo archivo
    wait_for_file_2 = FileSensor(
        task_id='wait_for_file_2',
        filepath='/opt/airflow/dags/input2.csv',
        poke_interval=30,
        timeout=600
    )

    # ✅ Job 3: Se ejecuta SOLO si los dos sensores anteriores terminan correctamente
    process_files = BashOperator(
        task_id='process_files',
        bash_command='echo "✅ Ambos archivos están listos. Ejecutando procesamiento final..."'
    )

    # 🔗 Dependencias: espera que ambos sensores terminen antes de ejecutar el último
    [wait_for_file_1, wait_for_file_2] >> process_files
