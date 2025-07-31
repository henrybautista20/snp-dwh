from pyspark.sql import SparkSession

# Crear sesión Spark
spark = SparkSession.builder.appName("WordCountExample").getOrCreate()

# Cargar datos de ejemplo
data = ["Hola mundo", "Hola Spark", "Spark es rápido"]
rdd = spark.sparkContext.parallelize(data)

# Contar palabras
word_counts = rdd.flatMap(lambda line: line.split(" ")) \
                 .map(lambda word: (word, 1)) \
                 .reduceByKey(lambda a, b: a + b)

# Mostrar resultados
for word, count in word_counts.collect():
    print(f"{word}: {count}")

spark.stop()
