
from pyspark import SparkContext

from pyspark.sql import SparkSession

def main():
    spark = spark = SparkSession.builder \
    .appName("Leer CSV desde HDFS") \
    .master("spark://192.168.1.137:7077")\
   .config(
        "spark.jars",
        "/var/snp-dwh/postgresql-42.7.3.jar,"
        "/var/snp-dwh/spark-excel_2.12-0.13.7.jar"
    ) \
    .getOrCreate()

    print("Hola a fg urban desde  PySpark run in a i r flow !")
    spark.stop()
    

if __name__ == "__main__":
    main()
