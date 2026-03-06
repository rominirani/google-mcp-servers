PROJECT_ID=$(gcloud config get-value project)
for i in {1..5}; do
   gcloud logging write checkout-service-logs '{"status": 500, "service": "checkout", "error": "ConnectionPoolExhausted: Unable to acquire aconnection from the pool within the timeout.", "transaction_id": "tx-99'$i'"}' --payload-type=json --severity=ERROR
done
echo "✅ Scenario 1 logs injected."
