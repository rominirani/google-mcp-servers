# Google MCP Servers

A collection of resources for working with fully-managed remote [Google MCP Servers](https://docs.cloud.google.com/mcp/overview). This repository contains configuration files, demo scenarios, and sample prompts to help you get started with Google's Model Context Protocol (MCP) integrations.

---

## What are Google MCP Servers?

Google MCP Servers are fully-managed, remote servers that expose Google Cloud and Google services as tools that AI agents (such as Gemini) can call. Using the [Model Context Protocol (MCP)](https://docs.cloud.google.com/mcp/overview), you can give AI agents the ability to query BigQuery, read Firestore documents, manage Compute Engine VMs, search Cloud Logs, call Google Maps APIs, and much more — all from natural language prompts.

---

## Repository Structure

```
.
├── README.md                        # This file
├── configuration/
│   └── gemini-cli-settings.json     # Ready-to-use Gemini CLI MCP server configuration
├── demos/
│   ├── README.md                    # Full setup guide and scenario catalog
│   ├── requirements.txt             # Python dependencies for demo setup scripts
│   ├── scenario_1.sh                # Inject sample logs for Scenario 1
│   ├── setup_scenario_2.py          # Setup data for Scenario 2
│   ├── setup_scenario_3.py          # Setup data for Scenario 3
│   ├── setup_scenario_4.py          # Setup data for Scenario 4
│   ├── setup_scenario_5.py          # Setup data for Scenario 5
│   ├── setup_scenario_6.py          # Setup data for Scenario 6
│   └── setup_scenario_7.py          # Setup data for Scenario 7
├── infographics/                    # Several infographics that you can use
└── prompts/
    └── getting-started.md           # 10 sample prompts across Google Cloud services
```

---

## Available MCP Servers

The following Google-managed MCP servers are covered in this repository:

| MCP Server | Endpoint | Authentication |
|---|---|---|
| **Developer Knowledge** | `https://developerknowledge.googleapis.com/mcp` | API Key |
| **Maps / Places** | `https://mapstools.googleapis.com/mcp` | API Key |
| **Cloud SQL** | `https://sqladmin.googleapis.com/mcp` | Google Credentials (OAuth) |
| **BigQuery** | `https://bigquery.googleapis.com/mcp` | Google Credentials (OAuth) |
| **Compute Engine** | `https://compute.googleapis.com/mcp` | Google Credentials (OAuth) |
| **Cloud Logging** | `https://logging.googleapis.com/mcp` | Google Credentials (OAuth) |
| **Cloud Monitoring** | `https://monitoring.googleapis.com/mcp` | Google Credentials (OAuth) |
| **Firestore** | `https://firestore.googleapis.com/mcp` | Google Credentials (OAuth) |
| **GKE** | `https://container.googleapis.com/mcp` | Google Credentials (OAuth) |

---

## Prerequisites

- A **Google Cloud Project** with billing enabled.
- **Google Cloud CLI (`gcloud`)** installed and authenticated:

  ```bash
  gcloud auth login
  gcloud auth application-default login
  gcloud config set project YOUR_PROJECT_ID
  ```

- **GCP Beta Components** for enabling managed MCP servers:

  ```bash
  gcloud components install beta
  ```

- **Required IAM Roles** on your identity:
  - `roles/serviceusage.serviceUsageAdmin` — to enable services and MCP
  - `roles/mcp.toolUser` — to make MCP tool calls
  - Service-specific roles as needed (e.g., `roles/bigquery.admin`, `roles/datastore.owner`, `roles/logging.admin`)

---

## Configuration

The [`configuration/gemini-cli-settings.json`](configuration/gemini-cli-settings.json) file provides a ready-to-use template for configuring multiple Google MCP servers in the [Gemini CLI](https://github.com/google-gemini/gemini-cli).

**File Location**: Place the contents into `~/.gemini/settings.json` (global) or `.gemini/settings.json` (project-local). Replace `YOUR_GCP_PROJECT_ID` and `YOUR_DEVELOPER_KNOWLEDGE_API_KEY` / `YOUR_GOOGLE_MAPS_API_KEY` with your actual values.

To verify the configuration after starting Gemini:

```bash
gemini
# then, inside the session:
/mcp list
```

---

## Demo Scenarios

The [`demos/`](demos/) folder contains a set of end-to-end scenarios that showcase multi-tool AI orchestration using Google Managed MCP Servers with Gemini. Each scenario includes a setup script to populate sample data and a suggested Gemini prompt.

| # | Scenario | Services Used |
|---|---|---|
| 1 | **Automated Incident Triage** | Cloud Logging, Developer Knowledge |
| 2 | **VIP Client Usage Analysis** | Firestore, BigQuery |
| 3 | **Real-time Campaign Health** | Firestore, Cloud Logging |
| 4 | **Threat Hunting** | BigQuery, Developer Knowledge |
| 5 | **Migration Performance Validation** | BigQuery, Developer Knowledge |
| 6 | **Dynamic Driver Routing** | Firestore, BigQuery, Google Maps |
| 7 | **Retail Expansion Analysis** | Firestore, BigQuery, Google Maps |

See the full setup guide and prompt catalog in [`demos/README.md`](demos/README.md).

---

## Infographics

The [`infographics/`](infographics/) folder contains visual guides and infographics covering a range of features around Google MCP Servers. These infographics have been primarily generated using NotebookLM.

| File | Description |
|---|---|
| [`FirestoreMCPServer.jpg`](infographics/FirestoreMCPServer.jpg) | Infographic on using the Firestore MCP Server |
| [`FirestoreMCPServer2.jpg`](infographics/FirestoreMCPServer2.jpg) | Infographic on using the Firestore MCP Server (part 2) |
| [`GoogleMCPServersSecurity.jpg`](infographics/GoogleMCPServersSecurity.jpg) | Infographic on Google MCP Servers security |
| [`StepByStepGuidetoGoogleMCPServers-March1-2026.png`](infographics/StepByStepGuidetoGoogleMCPServers-March1-2026.png) | Step-by-step visual guide to getting started with Google MCP Servers |

---

## Getting Started Prompts

The [`prompts/getting-started.md`](prompts/getting-started.md) file contains **10 natural language queries** that demonstrate the breadth of Google MCP integrations across:

- 📊 **Data & Analytics** — BigQuery public datasets, Firestore document writes
- 🏗️ **Infrastructure & Compute** — Compute Engine VM creation, GKE cluster listing
- 🗄️ **Database Administration** — Cloud SQL instance inspection and table creation
- 🔍 **Observability & Troubleshooting** — Cloud Logging error retrieval, Monitoring alert policies
- 🌍 **Real-World Integrations** — Google Maps Places search, multi-service route + weather queries

Each prompt includes the APIs to enable, required IAM roles, and any resource prerequisites needed to run it successfully.

---

## Contributing

Contributions are welcome! Feel free to open a pull request to add new prompts, demo scenarios, or configuration examples.

