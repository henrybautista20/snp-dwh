from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField, StringType, DoubleType, DateType
)

# Definición del schema exacto que me pasaste
schema = StructType([
    StructField("codigo_", StringType(), True),
    StructField("TIPO", StringType(), True),
    StructField("EJE", StringType(), True),
    StructField("NOMBRE_DEL_OBJETIVO", StringType(), True),
    StructField("NOMBRE_DE_LA_POLITICA", StringType(), True),
    StructField("META", StringType(), True),
    StructField("INDICADOR", StringType(), True),
    StructField("FUENTE_DE_INFORMACION", StringType(), True),
    StructField("GRUPO_DE_DESAGREGACION", StringType(), True),
    StructField("NIVEL_DE_DESAGREGACION", StringType(), True),
    StructField("CODIGO_GEOGRAFICO_DPA", StringType(), True),
    StructField("MES_ANIO", StringType(), True),
    StructField("FECHA", DateType(), True),
    StructField("ESTIMADOR", DoubleType(), True),
    StructField("ERROR_ESTANDAR", DoubleType(), True),
    StructField("LIMITE_INFERIOR", DoubleType(), True),
    StructField("LIMITE_SUPERIOR", DoubleType(), True),
    StructField("COEFICIENTE_DE_VARIACION", DoubleType(), True),
    StructField("NUMERADOR", DoubleType(), True),
    StructField("DENOMINADOR", DoubleType(), True),
    StructField("NOMBRE_DEL_EJE", StringType(), True),
    StructField("PERIODICIDAD_FICHA_METODOLOGICA", StringType(), True),
    StructField("FECHA_DE_TRANSFERENCIA_FICHA_METODOLOGICA", StringType(), True),
    StructField("DESAGREGACION_FICHA_METODOLOGICA", StringType(), True),
    StructField("PERIODICIDAD_DEL_DATO", StringType(), True)
])

# SparkSession con tus jars locales
jars = [
    "/var/snp-dwh/spark_jobs/jars/spark-excel_2.12-0.13.7.jar",
    "/var/snp-dwh/spark_jobs/jars/poi-4.1.2.jar",
    "/var/snp-dwh/spark_jobs/jars/poi-ooxml-4.1.2.jar",
    "/var/snp-dwh/spark_jobs/jars/xmlbeans-3.1.0.jar",
    "/var/snp-dwh/spark_jobs/jars/commons-math3-3.6.1.jar",
    "/var/snp-dwh/spark_jobs/jars/ooxml-schemas-1.4.jar",
    "/var/snp-dwh/spark_jobs/jars/postgresql-42.7.3.jar"
]

spark = SparkSession.builder \
    .appName("Leer Indicadores PND24-25") \
    .master("spark://192.168.1.137:7077")\
    .config("spark.jars", ",".join(jars)) \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()

# Ruta en HDFS (ajusta si cambias el archivo)
hdfs_path = "hdfs://192.168.1.137:8020/data/datos_pnd2425-13-05-2025_n.xlsx"

# Leer usando dataAddress para empezar desde la fila 3
df = spark.read.format("com.crealytics.spark.excel") \
    .option("header", "true") \
    .option("dataAddress", "'Indicadores PND24-25'!A3") \
    .schema(schema) \
    .load(hdfs_path)

# Mostrar esquema y algunas filas
df.printSchema()
df.show(5, truncate=False)
# Escribir en PostgreSQL
df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://192.168.1.137:5432/usuario_db") \
    .option("dbtable", "usuario_spark2") \
    .option("user", "airflow") \
    .option("password", "airflow") \
    .option("driver", "org.postgresql.Driver") \
    .mode("append") \
    .save()

print("✅ Registros insertados exitosamente en usuario_spark.")

