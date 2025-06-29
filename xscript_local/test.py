from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Leer Excel desde HDFS") \
    .master("spark://192.168.1.137:7077")\
    .config("spark.jars.packages", "com.crealytics:spark-excel_2.12:0.13.7") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()
hdfs_path = "hdfs://192.168.1.137:8020/data/usuarios.xlsx"

df = spark.read.format("com.crealytics.spark.excel") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(hdfs_path)

df.show(5)
