from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 6, 20),
    'email': ['gopi.daya@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
    'schedule_interval': '@monthly'
}

with DAG(dag_id='ETL-E-Verify',
        default_args=default_args,
        schedule_interval=None,
        tags=['evproject'],
        ) as dag:
        pass