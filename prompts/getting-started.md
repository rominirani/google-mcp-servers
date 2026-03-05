# Getting Started with basic prompts

Here are 10 natural language queries that demonstrate the power of the Google MCP integrations.

These examples highlight how you can use simple English to orchestrate complex cloud operations, replacing hundreds of lines of API boilerplate, authentication management, and JSON parsing with a single sentence.

_Please contribute to this list via a PR._


Each of these examples may require a one-time setup. The respective APIs and MCP Servers need to be enabled in the project. 
Once the APIs are enabled and permissions are granted to the MCP agent's identity, any additional role and/or one-time data creation is mentioned. 

Here is the exact groundwork required behind the scenes to make each of those 10 prompts work successfully.

📊 Data & Analytics (BigQuery & Firestore)

  1. "Run a query to count the number of penguins on each island in the BigQuery public dataset ml_datasets.penguins."
   * APIs to Enable: BigQuery API.
   * IAM Permissions: The agent's identity needs roles/bigquery.jobUser (to execute queries) and roles/bigquery.dataViewer (to read data).
   * Resource Prerequisites: You need an active billing account linked to the GCP project. Even though the bigquery-public-data dataset is external and
     free to read, BigQuery requires a billed project to charge for the compute resources used to run the query.

  2. "Add a new document to the 'users' collection in my default Firestore database with the fields 'name' as 'Alice' and 'role' as 'Admin'."
   * APIs to Enable: Cloud Firestore API.
   * IAM Permissions: The agent needs roles/datastore.user to read and write documents.
   * Resource Prerequisites: You must have initialized a Firestore database in the project (typically the (default) database) and selected its mode
     (Native or Datastore mode).

🏗️ Infrastructure & Compute (Compute Engine & GKE)

  3. "Create a new e2-medium Compute Engine VM instance named 'demo-web-server' in the us-central1-a zone."
   * APIs to Enable: Compute Engine API.
   * IAM Permissions: The agent needs roles/compute.instanceAdmin.v1. Additionally, because VMs use a default service account, the agent also needs
     roles/iam.serviceAccountUser to attach that identity to the VM.
   * Resource Prerequisites: The project must be linked to a valid billing account. A default VPC network must exist (or you must specify a custom one in
     the prompt).

  4. "List all my GKE clusters across all regions, and tell me the current node count and Kubernetes version for each."
   * APIs to Enable: Kubernetes Engine API.
   * IAM Permissions: The agent needs roles/container.clusterViewer.
   * Resource Prerequisites: To get a meaningful response, at least one GKE cluster must have been previously provisioned in the project.

🗄️ Database Administration (Cloud SQL)

  5. "What are the names, regions, and database versions of all the Cloud SQL instances currently running in this project?"
   * APIs to Enable: Cloud SQL Admin API.
   * IAM Permissions: The agent needs roles/cloudsql.viewer.
   * Resource Prerequisites: You must have at least one Cloud SQL instance actively running to yield results.

  6. "Create a sample mcp_users table in the on the '<YOUR_INSTANCE_NAME>' Cloud SQL Postgres database. Populate it with 10 sample records."
   * APIs to Enable: Cloud SQL Admin API.
   * IAM Permissions: The agent needs roles/cloudsql.viewer to view data.
   * Resource Prerequisites: 
       * The database instance name must already exist.

🔍 Observability & Troubleshooting (Logging & Monitoring)

  7. "Fetch the last 50 logs with a severity of 'ERROR' from Cloud Logging for this project."
   * APIs to Enable: Cloud Logging API.
   * IAM Permissions: The agent needs roles/logging.viewer.
   * Resource Prerequisites: Services in your project (like VMs, Cloud Run, or Cloud Functions) must be actively emitting structured logs. If the project
     is brand new and empty, this query will successfully run but return zero results.

  8. "Show me all the currently active Cloud Monitoring alert policies so I can review our notification configurations."
   * APIs to Enable: Cloud Monitoring API.
   * IAM Permissions: The agent needs roles/monitoring.viewer.
   * Resource Prerequisites: A user or administrator must have previously navigated to Cloud Monitoring to create a metrics workspace and set up at least
     one Alerting Policy (e.g., "CPU utilization > 80%"). 

🌍 Real-World Integrations (Maps, Places, & Weather)

  9. "Find the top-rated coffee shops near Golden Gate Park in San Francisco."
   * APIs to Enable: Places API (New) and potentially Geocoding API.
   * IAM/Auth Prerequisites: Unlike core GCP services that use service accounts natively, Maps APIs often rely on API Keys. The environment running the
     MCP server must be configured with a valid GOOGLE_MAPS_API_KEY (restricted appropriately for security) or set up for OAuth depending on the exact
     MCP implementation.
   * Resource Prerequisites: None, other than the API enablement.

  10. "Calculate the driving route from the Eiffel Tower to the Louvre Museum, and tell me what the weather is like at the destination right now."
   * APIs to Enable: Routes API, Geocoding API, and the respective Weather API backing the tool.
   * IAM/Auth Prerequisites: Similar to the Places prompt, this requires valid API keys or authenticated service accounts injected into the environment
     variables of the MCP server container/process.
   * Resource Prerequisites: This highlights the need for multi-tool schema alignment. The setup must ensure that the output format of the Routes/Places
     tool (like lat_lng objects) natively matches the input schema expected by the Weather tool, allowing the AI to pass variables between them
     seamlessly.
