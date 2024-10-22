# Airflow Connections Setup

This README provides instructions for configuring necessary connections in the Airflow UI, and additional key-value setups required for integration with services like PostgreSQL, Slack, Spark, and others.

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

| Field             | Value                  |
|-------------------|------------------------|
| **Conn Id**        | `slack_webhook`        |
| **Conn Type**      | `slackwebhook`         |
| **Host**           | _Leave empty_          |
| **Port**           | _Leave empty_          |
| **Is Encrypted**   | `False`                |
| **Is Extra Encrypted** | `False`            |
| **Description**    | Slack Webhook connection (Optional) |

---

### 5. `spark` (Spark)

| Field             | Value                  |
|-------------------|------------------------|
| **Conn Id**        | `spark`                |
| **Conn Type**      | `spark`                |
| **Host**           | `spark://spark`        |
| **Port**           | `7077`                 |
| **Is Encrypted**   | `False`                |
| **Is Extra Encrypted** | `False`            |
| **Description**    | Spark cluster connection (Optional) |

---

## Adding Key-Value Pairs in Airflow UI

You may also need to add certain key-value configurations in Airflow for specific use cases, like setting file paths or adding webhook URLs.

1. **Navigate to the Variables Page**  
   - In the Airflow UI, go to **Admin** > **Variables**.

2. **Add New Key-Value Pairs**  
   - Click the **"+"** button to add the following key-value pairs:

### Key-Value Pair Details

### 1. `container_path`

| Field             | Value                  |
|-------------------|------------------------|
| **Key**            | `container_path`       |
| **Value**          | `.`                    |
| **Is Encrypted**   | `False`                |
| **Description**    | (Optional) |

---

### 2. `path`

| Field             | Value                  |
|-------------------|------------------------|
| **Key**            | `path`                 |
| **Value**          | `/small_text.txt`      |
| **Is Encrypted**   | `False`                |
| **Description**    | (Optional) |

---

### 3. `slack_key`

| Field             | Value                  |
|-------------------|------------------------|
| **Key**            | `slack_key`            |
| **Value**          | `https://hooks.slack.com/services/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` |
| **Is Encrypted**   | `False`                |
| **Description**    | Slack webhook URL |

---

## Final Steps

- Once the connections and variables are added, they will be available for use within your Airflow DAGs.
- Make sure to reference these keys in your DAG scripts where necessary.

---

With this setup, your Airflow instance will be able to interact with PostgreSQL, Slack, Spark, and local filesystem resources, along with managing key variables like file paths and webhook URLs.
