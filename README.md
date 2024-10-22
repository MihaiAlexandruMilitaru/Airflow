# Airflow Connections Setup

This README provides instructions for configuring necessary connections in the Airflow UI to ensure integration with services like PostgreSQL, Slack, and Spark.

## Prerequisites

Ensure that your Airflow instance is up and running. Access the Airflow UI, typically available at `http://localhost:8080`.

## Adding Connections in Airflow UI

1. **Login to Airflow UI**
   - Open the Airflow web interface.
   - Navigate to **Admin** > **Connections** in the top menu.

2. **Add New Connections**
   - Click the **"+"** button on the right-hand side of the **Connections** page.
   - Fill in the connection details for each service, as outlined below.

## Connection Details

### 1. `fs_default` (Filesystem)

| Field             | Value                  |
|-------------------|------------------------|
| **Conn Id**        | `fs_default`           |
| **Conn Type**      | `fs`                   |
| **Host**           | _Leave empty_          |
| **Port**           | _Leave empty_          |
| **Is Encrypted**   | `False`                |
| **Is Extra Encrypted** | `False`            |
| **Description**    | Default filesystem connection (Optional) |

---

### 2. `postgres_default` (PostgreSQL)

| Field             | Value                  |
|-------------------|------------------------|
| **Conn Id**        | `postgres_default`     |
| **Conn Type**      | `postgres`             |
| **Host**           | `postgres` (or your actual host) |
| **Port**           | `5432`                 |
| **Is Encrypted**   | `False`                |
| **Is Extra Encrypted** | `False`            |
| **Description**    | PostgreSQL default connection (Optional) |

---

### 3. `slack_conn` (Slack)

| Field             | Value                  |
|-------------------|------------------------|
| **Conn Id**        | `slack_conn`           |
| **Conn Type**      | `slack`                |
| **Host**           | _Leave empty_          |
| **Port**           | _Leave empty_          |
| **Is Encrypted**   | `False`                |
| **Is Extra Encrypted** | `False`            |
| **Description**    | Slack connection (Optional) |

---

### 4. `slack_webhook` (Slack Webhook)

| Field             | Value                  
