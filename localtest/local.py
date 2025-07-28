from pyspark import SparkContext
from pyspark.sql import SparkSession

# ✅ Evitar SparkContext previo (solo relevante si lo corres en notebooks)
try:
    sc = SparkContext._active_spark_context
    if sc is not None:
        sc.stop()
        SparkContext._active_spark_context = None
except Exception:
    pass

def main():
    # ✅ El driver es local, los w