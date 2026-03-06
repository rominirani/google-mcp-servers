# Google Managed MCP Servers - Demo Scenarios

This project contains a collection of demo scenarios for testing and showcasing the power of **Google Managed MCP Servers** with Gemini. These scenarios demonstrate multi-tool orchestration across Firestore, BigQuery, Cloud Logging, Google Maps, and Developer Knowledge.

## 🛠 Project Setup

Follow these steps to configure your environment and enable the necessary Google Managed MCP servers.

### 1. Prerequisites

- **Google Cloud Project**: A project with billing enabled.
- **Google Cloud CLI (`gcloud`)**: Installed and authenticated.

  ```bash
  gcloud auth login
  gcloud auth application-default login
  gcloud config set project YOUR_PROJECT_ID
  ```

- **GCP Beta Components**:

  ```bash
  gcloud components install beta
  ```

### 2. Required IAM Roles

Ensure your identity (User or Service Account) has the following roles:

- `roles/serviceusage.serviceUsageAdmin` (to enable services and MCP)
- `roles/mcp.toolUser` (to make MCP tool calls)
- Service-specific roles: `roles/bigquery.admin`, `roles/datastore.owner`, `roles/logging.admin`.

### 3. Enable APIs & Managed MCP Servers

You must enable both the base API service and its corresponding Managed MCP server for each tool used in the scenarios.

```bash
# Enable Base Services
gcloud services enable \
  firestore.googleapis.com \
  bigquery.googleapis.com \
  logging.googleapis.com \
  mapstools.googleapis.com \
  developerknowledge.googleapis.com

# Enable Managed MCP Servers
gcloud beta services mcp enable firestore.googleapis.com
gcloud beta services mcp enable bigquery.googleapis.com
gcloud beta services mcp enable logging.googleapis.com
gcloud beta services mcp enable mapstools.googleapis.com
gcloud beta services mcp enable developerknowledge.googleapis.com
```

### 4. Create API Key (For Developer Knowledge)

The Developer Knowledge MCP server requires an API Key for authentication.

1. **Create the API Key**:

   ```bash
   gcloud services api-keys create --project=YOUR_PROJECT_ID --display-name="Developer Knowledge Key"
   ```

2. **Note the Key**: The command output will contain the key string (`response.keyString`). You will need this for the Gemini CLI configuration.
3. **Restricting the Key (Best Practice)**: It is highly recommended to restrict this key to only the "Developer Knowledge API" in the [Google Cloud Console](https://console.cloud.google.com/apis/credentials).

### 5. Initialize Firestore

If not already initialized, create the database in Native mode:

```bash
gcloud firestore databases create --location=us-central1 --type=firestore-native
```

### 5. Local Python Environment

1. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv mcp_env
   source mcp_env/bin/activate
   ```

2. **Install dependencies**:

   ```bash
   pip install google-cloud-firestore google-cloud-bigquery
   ```

### 6. Gemini CLI Configuration

To use these MCP servers in the Gemini CLI, you must add them to your `settings.json` file.

**File Location**: `~/.gemini/settings.json` (Global) or `.gemini/settings.json` (Project-local).

#### Manual JSON Configuration (Recommended)

Add the following to the `mcpServers` block in your `settings.json`. Replace `YOUR_PROJECT_ID` with your actual project ID.

```json
{
  "mcpServers": {
    "google-firestore": {
      "httpUrl": "https://firestore.googleapis.com/mcp",
      "authProviderType": "google_credentials",
      "oauth": {
        "scopes": ["https://www.googleapis.com/auth/cloud-platform"]
      },
      "headers": {
        "X-goog-user-project": "YOUR_PROJECT_ID"
      }
    },
    "google-bigquery": {
      "httpUrl": "https://bigquery.googleapis.com/mcp",
      "authProviderType": "google_credentials",
      "oauth": {
        "scopes": ["https://www.googleapis.com/auth/cloud-platform"]
      },
      "headers": {
        "X-goog-user-project": "YOUR_PROJECT_ID"
      }
    },
    "google-logging": {
      "httpUrl": "https://logging.googleapis.com/mcp",
      "authProviderType": "google_credentials",
      "oauth": {
        "scopes": ["https://www.googleapis.com/auth/cloud-platform"]
      },
      "headers": {
        "X-goog-user-project": "YOUR_PROJECT_ID"
      }
    },
    "google-maps": {
      "httpUrl": "https://mapstools.googleapis.com/mcp",
      "headers": {
        "X-Goog-Api-Key": "YOUR_GOOGLE_MAPS_API_KEY"
      }
    },
    "google-developer-knowledge": {
      "httpUrl": "https://developerknowledge.googleapis.com/mcp",
      "headers": {
        "X-Goog-Api-Key": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

#### Verify Configuration

Start a Gemini session and use slash commands to verify your tools and MCP servers are connected:

1. **Start Gemini**:

   ```bash
   gemini
   ```

2. **List MCP Servers**:
   To see detailed connection status for your MCP servers, type:

   ```plaintext
   /mcp list
   ```

---

## 📋 Scenario Catalog

### 1. Automated Incident Triage (DevOps)

**Use Case**: A sudden spike in errors is reported. The agent pulls error payloads from Cloud Logging, identifies the exception, and searches Google's documentation for a fix.

- **Setup**:

  ```bash
  # Run the injection script
  ./scenario_1.sh
  ```

- **Gemini Prompt**:
  > "Our monitoring is alerting on the checkout service. Fetch the last 5 ERROR logs from the 'checkout-service-logs' in Cloud Logging. Extract the specific error message text from the JSON payload. Once you have the error message, search the Google Developer documentation for troubleshooting that specific error in Cloud Run to give me a summary of how to fix it."

### 2. VIP Client Usage Analysis (Sales/CS)

**Use Case**: Retrieve client metadata from Firestore, query API usage from BigQuery, and summarize for a renewal call.

- **Setup**:

  ```bash
  python3 setup_scenario_2.py
  ```

- **Gemini Prompt**:
  > "I have a renewal call with 'Acme Corp'. Read their client profile from the 'clients/acme_corp' document in Firestore to find their 'tenant_id' and current 'tier'. Then, use that tenant ID to run a BigQuery SQL query against the api_metrics.usage_logs table to sum up their total 'api_calls'. Give me a short summary of their profile and total usage."

### 3. Real-time Campaign Health (Marketing)

**Use Case**: Verify a campaign is active in Firestore and check Cloud Logging for "invalid promo code" errors.

- **Setup**:

  ```bash
  python3 setup_scenario_3.py
  ```

- **Gemini Prompt**:
  > "Check the 'campaigns/spring_promo' document in Firestore to confirm what the exact promo 'code' is and if 'is_active' is true. If it is active, search Cloud Logging for the last 50 logs in 'promo-service-logs'. Tell me if you see any WARNING or ERROR logs associated with that specific promo code."

### 4. Threat Hunting (Security)

**Use Case**: Query BigQuery for failed logins from a suspicious IP and search Developer Knowledge for blocking instructions.

- **Setup**:

  ```bash
  python3 setup_scenario_4.py
  ```

- **Gemini Prompt**:
  > "Our system flagged IP '203.0.113.45'. Write and execute a BigQuery SQL query against security_audit.login_events to count exactly how many 'FAILED' login attempts originated from this IP address. After you get the count, search the Developer Knowledge documents for 'Cloud Armor rate limiting block IP' and give me the exact gcloud command syntax needed to block this IP."

### 5. Migration Performance Validation (Ops/Eng)

**Use Case**: Compare latencies in BigQuery after a database migration and look up optimization if performance regressed.

- **Setup**:

  ```bash
  python3 setup_scenario_5.py
  ```

- **Gemini Prompt**:
  > "We just rolled out the 'firestore_v2' architecture. Run a BigQuery SQL query on `app_performance.page_loads` to find the average 'latency_ms' grouped by 'architecture'. If 'firestore_v2' is slower than 'legacy', search the Developer Knowledge docs for 'Firestore query performance optimization best practices' and summarize the top 3 recommendations for the engineering team."

### 6. Dynamic Driver Routing (Logistics)

**Use Case**: Fetch delivery destination from Firestore, driver's real-time coordinates from BigQuery, and calculate the route using Google Maps.

- **Setup**:

  ```bash
  python3 setup_scenario_6.py
  ```

- **Gemini Prompt**:
  > "We need to dispatch delivery 'del_001'. First, look up the 'destination' for this delivery in the Firestore 'deliveries' collection. Next, query the BigQuery `logistics.driver_telemetry` table to find the latest latitude and longitude for 'driver_88'. Finally, use Google Maps to calculate the driving route, distance, and duration from the driver's lat/lng coordinates to the delivery destination."

### 7. Retail Expansion Analysis (Strategy)

**Use Case**: Evaluate a proposed cafe location by checking neighborhood foot traffic in BigQuery and scouting competition nearby using Maps.

- **Setup**:

  ```bash
  python3 setup_scenario_7.py
  ```

- **Gemini Prompt**:
  > "Read the proposed location 'loc_alpha' from the 'proposed_locations' collection in Firestore to get its 'address' and 'neighborhood'. Then, query BigQuery retail_analytics.neighborhood_metrics to get the 'foot_traffic_score' for that specific neighborhood. Finally, use Google Maps to search for top-rated 'coffee shops' near that exact address so we can assess the local competition."
