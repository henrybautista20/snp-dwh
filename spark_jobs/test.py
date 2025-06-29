from pyspark.sql import SparkSession
import pandas as pd
jars = [
    "/var/snp-dwh/spark-excel_2.12-0.13.7.jar",
    "/var/snp-dwh/poi-4.1.2.jar",
    "/var/snp-dwh/poi-ooxml-4.1.2.jar",
    "/var/snp-dwh/xmlbeans-3.1.0.jar",
    "/var/snp-dwh/commons-math3-3.6.1.jar",
    "/var/snp-dwh/ooxml-schemas-1.4.jar"
]

spark = SparkSession.builder \
    .appName("Leer Excel desde HDFS") \
    .config("spark.jars", ",".join(jars)) \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()

hdfs_path = "hdfs://192.168.1.137:8020/data/datos_pnd2425-13-05-2025_n.xlsx"

# Leemos sólo la hoja "Indicadores PND24-25"
df_pnd = spark.read.format("com.crealytics.spark.excel") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("sheetName", "Indicadores PND24-25") \
    .load(hdfs_path)

# Echa un vistazo a las primeras filas
df_pnd.show(10, truncate=False)
