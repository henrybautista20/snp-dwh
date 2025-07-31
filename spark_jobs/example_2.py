from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField, StringType, DoubleType, DateType
)


def main():
    # ✅ El driver es local, los workers están en Docker
    spark = SparkSession.builder \
    .appName("Leer Indicadores PND24-25") \
    .config("spark.driver.memory", "2g") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()

    print("🔥 Hola desde urban, ejecutando con spark-submit en el cluster!")

    # Datos de ejemplo
    datos = [("1", "Juan", "Quito"),
             ("2", "Ana", "Guayaquil"),
             ("3", "Luis", "Cuenca")]
    columnas = ["id", "nombre", "ciudad"]

    df = spark.createDataFrame(datos, columnas)
    df.show()

    spark.stop()

if __name__ == "__main__":
    main()
