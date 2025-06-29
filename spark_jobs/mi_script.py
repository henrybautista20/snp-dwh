from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

# Crear sesión de Spark conectada al cluster
spark = SparkSession.builder \
    .appName("Leer CSV desde HDFS") \
    .getOrCreate()

# Ruta HDFS del archivo
hdfs_path = "hdfs://hadoop-namenode:8020/data/usuarios.csv"

# Nota: Asegúrate de que el nombre del nodo y el puerto coincidan con tu configuración de HDFS
# Si estás usando un contenedor, puede que necesites usar la IP del contenedor en
hdfs_path = "hdfs://192.168.1.137:8020/data/usuarios.csv" # para uns hot local

# caso de que localhost no funcione.
# Crear esquema
schema = StructType([
    StructField("nombre", StringType(), True),
    StructField("correo", StringType(), True)
])
# Leer CSV desde HDFS
df = spark.read.csv(hdfs_path, header=True, schema = schema )



# Mostrar contenido
df.show()


print("✅ Registros insertados exitosamente en usuario_spark.")