import os
import time
from google.cloud import firestore, bigquery

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

# 1. Setup Firestore Delivery Document
db = firestore.Client(project=project_id)
db.collection("deliveries").document("del_001").set({
    "destination": "Coit Tower, San Francisco, CA",
    "status": "pending",
    "assigned_driver": "driver_88"
})

# 2. Setup BigQuery Telemetry Data
bq = bigquery.Client(project=project_id)
dataset_id = f"{project_id}.logistics"
bq.create_dataset(bigquery.Dataset(dataset_id), exists_ok=True)

table_id = f"{dataset_id}.driver_telemetry"
schema = [
    bigquery.SchemaField("driver_id", "STRING"),
    bigquery.SchemaField("lat", "FLOAT"),
    bigquery.SchemaField("lng", "FLOAT"),
    bigquery.SchemaField("timestamp", "TIMESTAMP")
]
bq.create_table(bigquery.Table(table_id, schema=schema), exists_ok=True)

print("Waiting 5 seconds for BigQuery table to initialize...")
time.sleep(5)

rows = [{"driver_id": "driver_88", "lat": 37.8086, "lng": -122.4098, "timestamp": "2026-03-05T10:00:00Z"}]
bq.insert_rows_json(table_id, rows)
print("✅ Scenario 6 data created in Firestore and BigQuery.")
