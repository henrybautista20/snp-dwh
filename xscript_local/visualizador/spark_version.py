# run_spark_local_excel.py
import os
import sys
import findspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# 1) Initialize PySpark (optional if pyspark is already on PATH)
findspark.init()

from pyspark.sql import SparkSession

# ---- Adjust these ----
BASE = "/home/henryx/urban/snp-dwh/spark_jobs"
LOCAL_JARS = ",".join([
    f"{BASE}/jars/spark-excel_2.12-0.13.7.jar",
    f"{BASE}/jars/poi-4.1.2.jar",
    f"{BASE}/jars/poi-ooxml-4.1.2.jar",
    f"{BASE}/jars/xmlbeans-3.1.0.jar",
    f"{BASE}/jars/commons-math3-3.6.1.jar",
    f"{BASE}/jars/ooxml-schemas-1.4.jar",
    f"{BASE}/jars/postgresql-42.7.3.jar",
])

# Use the real, exact file name (watch out: in your text there’s a stray space after the dash!)
# BAD: '...- 12-06-2025_vcf.xlsx'
# GOOD: '...-12-06-2025_vcf.xlsx'
local_excel_path = "/home/henryx/urban/snp-dwh/xscript_local/visualizador/datos_pnd2425- 12-06-2025_vcf.xlsx"

# If you truly want HDFS instead, use a proper HDFS URL and make sure Hadoop client configs are visible to Spark:
# hdfs_excel_path = "hdfs://172.18.21.152:8020/data/datos_pnd2425-12-06-2025_vcf_l1.xlsx"

app_name = "ExcelReaderLocal"

# 2) Build SparkSession for local use

spark = (
    SparkSession.builder
    .appName("SimplePySparkDataFrame")
    .master("local[*]")  # local mode
    .config("spark.jars", LOCAL_JARS)
    .config("spark.driver.memory", "4g")       # 4 GB for driver
    .config("spark.executor.memory", "4g")     # 4 GB for executors
    .config("spark.sql.shuffle.partitions", "8")  # optional: fewer partitions for local
    .getOrCreate()
)
df = (
    spark.read.format("com.crealytics.spark.excel")
    .option("header", "true")
    .option("dataAddress", "'Indicadores PND24-25'!A3")
    .load(local_excel_path))

# 4) Quick checks
df.printSchema()
df.show(10, truncate=False)
print("Row count:", df.count())
spark.stop()
