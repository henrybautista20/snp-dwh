#!/usr/bin/env python3

# 1) Limpiar SparkContext antiguo si existe
from pyspark import SparkContext
try:
    sc = SparkContext._active_spark_context  # comprueba si hay uno activo
    if sc is not None:
        sc.stop()
        SparkContext._active_spark_context = None
except Exception:
    pass

# 2) Ahora crea tu SparkSession con total normalidad
from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("SimplePrintJob") \
        .getOrCreate()

    print("¡Hola desde PySpark!")
    spark.stop()

if __name__ == "__main__":
    main()
