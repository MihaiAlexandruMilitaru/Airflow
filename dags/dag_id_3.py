from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator, ShortCircuitOperator
from resources import *
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

def check_table_exists(table_name):
    hook = PostgresHook(postgres_conn_id="postgres_default")
    sql = f"SELECT table_name FROM information_schema.tables WHERE table_name = '{table_name}'"
    query = hook.get_first(sql)
    if query:
        return "insert_new_row"
    return "create_table"

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
        python_callable=check_table_exists,
        op_args=["table_name"],
        dag=dag
    )
    task3 = SQLExecuteQueryOperator(
        task_id="create_table",
        conn_id="postgres_default",
        sql="""CREATE TABLE table_name(custom_id integer NOT NULL,
                        user_name VARCHAR (30) NOT NULL, timestamp TIMESTAMP NOT NULL);""",
        dag=dag
    )
    task4 = SQLExecuteQueryOperator(
        task_id="insert_new_row",
        conn_id="postgres_default",
        trigger_rule="none_failed",
        sql="""INSERT INTO table_name(custom_id, user_name, timestamp)
               VALUES (1, 'user1', CURRENT_TIMESTAMP);""",
        dag=dag
    )
    task5 = PythonOperator(
        task_id="query_table",
        python_callable=push_xcom,
        provide_context=True,
        dag=dag
    )


    # if table exists, insert new row, else create table and insert new row
    task1 >> task2
    task2 >> task3 >> task4 >> task5
    task2 >> task4 >> task5
