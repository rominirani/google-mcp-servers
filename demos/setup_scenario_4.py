import os
import time
from google.cloud import bigquery

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
bq = bigquery.Client(project=project_id)
dataset_id = f"{project_id}.security_audit"
bq.create_dataset(bigquery.Dataset(dataset_id), exists_ok=True)
table_id = f"{dataset_id}.login_events"
schema = [
    bigquery.SchemaField("ip_address", "STRING"),
    bigquery.SchemaField("status", "STRING"),
]
bq.create_table(bigquery.Table(table_id, schema=schema), exists_ok=True)
print("Waiting 5 seconds for BigQuery table to initialize...")
time.sleep(5)
rows = [
    {"ip_address": "203.0.113.45", "status": "FAILED"},
    {"ip_address": "203.0.113.45", "status": "FAILED"},
    {"ip_address": "203.0.113.45", "status": "FAILED"},
    {"ip_address": "198.51.100.2", "status": "SUCCESS"},
]
bq.insert_rows_json(table_id, rows)
print("✅ Scenario 4 security audit data created in BigQuery.")