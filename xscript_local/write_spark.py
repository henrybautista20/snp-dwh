from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql import Row

# Crear sesión de Spark con el conector JDBC
spark = SparkSession.builder \
    .appName("Insertar usuarios desde Spark") \
    .config("spark.jars", "/var/snp-dwh/postgresql-42.7.3.jar") \
    .getOrCreate()

# Crear datos manualmente
datos = [
    ("Mario López", "mario.lopez@example.com"),
    ("Julia Ríos", "julia.rios@example.com"),
    ("Carlos Álvarez", "carlos.alvarez@example.com"),
    ("Sofía Naranjo", "sofia.naranjo@example.com"),
]

# Crear esquema
schema = StructType([
    StructField("nombre", StringType(), True),
    StructField("correo", StringType(), True)
])

# Crear DataFrame
df = spark.createDataFrame(datos, schema)

# Mostrar contenido
df.show()

# Escribir en PostgreSQL
df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://127.0.0.1:5432/airflow") \
    .option("dbtable", "usuario_spark") \
    .option("user", "airflow") \
    .option("password", "airflow") \
    .option("driver", "org.postgresql.Driver") \
    .mode("append") \
    .save()

print("✅ Registros insertados exitosamente en usuario_spark.")
