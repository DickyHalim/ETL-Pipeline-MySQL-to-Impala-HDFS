import pandas as pd
from pyspark.sql import SparkSession

jar_path = "/home/cdsw/mysql-connector-j-8.0.33.jar"

spark = SparkSession.builder \
    .appName("MySQL to Impala") \
    .config("spark.jars", jar_path) \
    .config("spark.driver.extraClassPath", jar_path) \
    .config("spark.executor.extraClassPath", jar_path) \
    .getOrCreate()
    
mysql_url = "jdbc:mysql://your_mysql_ip_address:your_my_sql_port/your_database_name"\

mysql_properties = {
    "user": "xxx", #replace with your mysql username
    "password": "xxx", #replace with your mysql password
    "driver": "com.mysql.cj.jdbc.Driver"
}

df_mysql = spark.read.jdbc(
    url=mysql_url,
    table="your_table_name_in_mysql",
    properties=mysql_properties
)

df_mysql.show()

spark.sql("TRUNCATE TABLE impala_database.impala_table") #replace with your impala database and table

df_mysql.write \
    .mode("append") \
    .insertInto("impala_database.impala_table")