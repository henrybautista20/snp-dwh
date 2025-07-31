import re
import time
from pyspark.sql import SparkSession

# === 1. Leer archivo normalmente con open() ===
file_path = "/opt/spark-apps/rvg_2004.txt"

start_total = time.time()  # ⏳ tiempo total desde el inicio

try:
    with open(file_path, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    print(f"✅ Archivo cargado correctamente: {len(lineas)} líneas")
except FileNotFoundError:
    print("❌ El archivo no existe en la ruta especificada.")
    exit(1)
except PermissionError:
    print("❌ No tienes permisos para leer este archivo.")
    exit(1)
except Exception as e:
    print(f"⚠️ Error al leer el archivo: {e}")
    exit(1)

# === 2. Crear sesión Spark ===
start_spark = time.time()
spark = SparkSession.builder \
    .appName("WordCountRVG") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()
print(f"⏳ Tiempo creación SparkSession: {time.time() - start_spark:.2f} s")

# === 3. Crear RDD a partir de la lista de líneas ===
start_rdd = time.time()
rdd = spark.sparkContext.parallelize(lineas)
for i in range(8):
    rdd=rdd+rdd
#rdd = rdd.flatMap(lambda x: [x]*256)
print(f"⏳ Tiempo paralelización: {time.time() - start_rdd:.2f} s")

# === 4. Procesamiento: limpiar palabras ===
def limpiar_palabra(p):
    return re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]", "", p).lower()

# Lista de palabras vacías comunes en español (opcional)
stopwords = {"y","de","que","el","la","en","a","los","se","del","un","por","con","no","una","su","al","lo","como","más","pero","sus","le","ya","o","este","sí","porque","esta","entre","cuando","muy","sin","sobre","también","me","hasta","hay","donde","quien","desde","todo","nos","durante","todos","uno","les","ni","contra","otros","ese","eso","ante","ellos","e","esto","mí","antes","algunos","qué","unos","yo","otro","otras","otra"}

# === 5. Conteo de palabras con Spark ===
start_job = time.time()
word_counts = (
    rdd.flatMap(lambda line: line.strip().split(" "))            
       .map(lambda word: limpiar_palabra(word))                  
       .filter(lambda w: w != "" and w not in stopwords)         
       .map(lambda word: (word, 1))
       .reduceByKey(lambda a, b: a + b)
)
print(f"⏳ Tiempo transformaciones Spark: {time.time() - start_job:.2f} s")

# === 6. Mostrar las 20 palabras más frecuentes ===
start_action = time.time()
top20 = word_counts.takeOrdered(20, key=lambda x: -x[1])
print(f"⏳ Tiempo acción (takeOrdered): {time.time() - start_action:.2f} s")

print("\n🔝 Top 20 palabras más frecuentes:")
for palabra, cantidad in top20:
    print(f"{palabra}: {cantidad}")

# === 7. Finalizar Spark ===
spark.stop()

# === 8. Tiempo total ===
print(f"\n✅ Tiempo total ejecución: {time.time() - start_total:.2f} s")
