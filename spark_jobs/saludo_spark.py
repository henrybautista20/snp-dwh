
from pyspark import SparkContext
try:
    sc = SparkContext._active_spark_context  
    if sc is not None:
        sc.stop()
        SparkContext._active_spark_context = None
except Exception:
    pass

from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("SimplePrintJob") \
        .getOrCreate()

    print("Hola urban desde  PySpark run in a i r flow !")
    spark.stop()

if __name__ == "__main__":
    main()
