from airflow import DAG
from airflow.hooks.base import BaseHook
from airflow.models import Variable
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.slack.notifications.slack import SlackNotifier, send_slack_notification
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from slack_sdk.errors import SlackApiError

from resources import *

webhook = Variable.get('slack_key')

slack_webhook_token = Variable.get("slack_key")

with DAG(
        dag_id="slack_dag",
        start_date=config["dag_id_1"]["start_date"],
        schedule=config["dag_id_1"]["schedule_interval"]
) as dag:
    task1 = SlackWebhookOperator(
        task_id='slack',
        message="Hello from your app!",
        slack_webhook_conn_id="slack_webhook"
    )
    task2 = EmptyOperator(
        task_id="empty"
    )
    task1 >> task2