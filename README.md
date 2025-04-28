# ETL-Pipeline-MySQL-to-Impala-HDFS
This project contains a simple ETL script that extracts data from a MySQL database, transforms it into a Spark DataFrame, and loads it into an Impala table (HDFS storage).
It is useful for data warehousing, analytics, and reporting use cases where data needs to be moved from OLTP systems to big data platforms.

🛠 Architecture
Extract: Read data from a MySQL table using JDBC.
Transform: (Optional) Spark DataFrame operations (can be customized).
Load: Write the data into an Impala-managed table.

📋 Prerequisites
1. Apache Spark installed and configured.
2. MySQL JDBC Driver (mysql-connector-j-8.0.33.jar).
3. Access to:
  a. MySQL database (with network/firewall permissions).
  b. Impala cluster and HDFS (via Spark and Hive Metastore).

⚙️ Setup
1. Place the MySQL JDBC .jar file in your working directory (or adjust the path in the script).

2. Update the following variables in the script:
  a. your_mysql_ip_address
  b. your_my_sql_port
  c. your_database_name
  d. your_table_name_in_mysql
  e. MySQL user and password
  f. Target impala_database.impala_table

3. Submit or run the Spark job in your environment (CDSW, Jupyter, local Spark, etc.)
