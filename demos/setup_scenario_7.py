import os
import time
from google.cloud import firestore, bigquery

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

# 1. Setup Firestore Proposed Location
db = firestore.Client(project=project_id)
db.collection("proposed_locations").document("loc_alpha").set({
    "address": "1000 4th St, San Francisco, CA",
    "neighborhood": "Mission Bay",
    "sq_ft": 1500
})

# 2. Setup BigQuery Neighborhood Metrics
bq = bigquery.Client(project=project_id)
dataset_id = f"{project_id}.retail_analytics"
bq.create_dataset(bigquery.Dataset(dataset_id), exists_ok=True)

table_id = f"{dataset_id}.neighborhood_metrics"
schema = [
    bigquery.SchemaField("neighborhood", "STRING"),
    bigquery.SchemaField("foot_traffic_score", "INTEGER")
]
bq.create_table(bigquery.Table(table_id, schema=schema), exists_ok=True)

print("Waiting 5 seconds for BigQuery table to initialize...")
time.sleep(5)

rows = [{"neighborhood": "Mission Bay", "foot_traffic_score": 85}]
bq.insert_rows_json(table_id, rows)
print("✅ Scenario 7 data created in Firestore and BigQuery.")
