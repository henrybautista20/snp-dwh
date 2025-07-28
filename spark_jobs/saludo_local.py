from pyspark import SparkContext
from pyspark.sql import SparkSession

# Asegúrate de no tener un contexto previo
try:
    sc = SparkContext._active_spark_context
    if sc is not None:
        sc.stop()
        SparkContext._active_spark_context = None
except Exception:
    pass
import findspark
findspark.init()

from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
    .appName("LocalNotebookApp1") \
    .getOrCreate()

    print("🔥 Hola desde urban, ejecutando con spark-submit en el cluster!")

    datos = [("1", "Juan", "Quito"),
             ("2", "Ana", "Guayaquil"),
             ("3", "Luis", "Cuenca")]
    columnas = ["id", "nombre", "ciudad"]

    df = spark.createDataFrame(datos, columnas)
    df.show()

    spark.stop()

if __name__ == "__main__":
    main()
