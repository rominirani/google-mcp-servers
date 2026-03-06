import os
import time
from google.cloud import firestore, bigquery

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

# Setup Firestore

db = firestore.Client(project=project_id)
db.collection("campaigns").document("spring_promo").set({
    "is_active": True, "code": "SPRING20"
})

print("✅ Scenario 3 data created in Firestore.")