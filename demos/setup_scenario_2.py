import os
import time
from google.cloud import firestore, bigquery

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
# Setup Firestore
db = firestore.Client(project=project_id)
db.collection("clients").document("acme_corp").set({
    "client_name": "Acme Corp", "tenant_id": "TENANT_994", "tier": "Standard"
})
# Setup BigQuery
bq = bigquery.Client(project=project_id)
dataset_id = f"{project_id}.api_metrics"
bq.create_dataset(bigquery.Dataset(dataset_id), exists_ok=True)
table_id = f"{dataset_id}.usage_logs"
schema = [
    bigquery.SchemaField("tenant_id", "STRING"),
    bigquery.SchemaField("api_calls", "INTEGER"),
]
bq.create_table(bigquery.Table(table_id, schema=schema), exists_ok=True)
print("Waiting 5 seconds for BigQuery table to initialize...")
time.sleep(5) # BQ needs a moment before accepting streaming inserts
rows = [
    {"tenant_id": "TENANT_994", "api_calls": 45000},
    {"tenant_id": "TENANT_994", "api_calls": 52000},
]
bq.insert_rows_json(table_id, rows)