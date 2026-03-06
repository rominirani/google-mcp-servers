import os
import time
from google.cloud import bigquery

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
bq = bigquery.Client(project=project_id)
dataset_id = f"{project_id}.app_performance"
bq.create_dataset(bigquery.Dataset(dataset_id), exists_ok=True)
table_id = f"{dataset_id}.page_loads"
schema = [
    bigquery.SchemaField("architecture", "STRING"),
    bigquery.SchemaField("latency_ms", "INTEGER"),
]
bq.create_table(bigquery.Table(table_id, schema=schema), exists_ok=True)
print("Waiting 5 seconds for BigQuery table to initialize...")
time.sleep(5)
rows = [
    {"architecture": "legacy", "latency_ms": 120},
    {"architecture": "legacy", "latency_ms": 135},
    {"architecture": "firestore_v2", "latency_ms": 450}, # Simulating regression
    {"architecture": "firestore_v2", "latency_ms": 480},
]
bq.insert_rows_json(table_id, rows)
print("✅ Scenario 5 performance data created in BigQuery.")
