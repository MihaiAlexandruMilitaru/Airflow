from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator, ShortCircuitOperator
from resources import *


def push_xcom(ti):
    ti.xcom_push(key="log", value=f"{ti.run_id} ended")


with DAG(
        dag_id="dag_id_3",
        start_date=config["dag_id_3"]["start_date"],
        schedule=config["dag_id_3"]["schedule_interval"]
) as dag:
    task1 = PythonOperator(
        task_id="log_database_connection",
        python_callable=log_context,
        op_kwargs={"dag_id": "dag_id_3", "database": "airflow"},
        dag=dag
    )
    task2 = BranchPythonOperator(
        task_id="check_if_table_exists",
        python_callable=branch_condition,
        dag=dag
    )
    task3 = EmptyOperator(
        task_id="create_table",
        dag=dag
    )
    task4 = EmptyOperator(
        task_id="insert_new_row",
        trigger_rule='none_failed',
        dag=dag
    )
    task5 = PythonOperator(
        task_id="query_table",
        python_callable=push_xcom,
        provide_context=True,
        dag=dag
    )


    task1 >> task2
    task2 >> task3
    task3 >> task4
    task2 >> task4
    task4 >> task5