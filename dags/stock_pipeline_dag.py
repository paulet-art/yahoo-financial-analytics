from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

import sys

sys.path.append('/opt/airflow/src')

from ingest_data import run
from config import BANK_STOCKS

default_args = {
    "owner": "paulet",
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
}

def run_stock_pipeline():
    run(BANK_STOCKS)

with DAG(
    dag_id="stock_data_pipeline",
    default_args=default_args,
    description="Financial stock ingestion pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    ingest_task = PythonOperator(
        task_id="run_ingestion",
        python_callable=run_stock_pipeline
    )

    ingest_task