import numpy as np
# parche por si sigues con el np.NaN issue
np.NaN = np.nan

import pyspark.pandas as ps
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType, DateType

# (recrea o usa tu SparkSession ya configurada con los JARs)
spark = SparkSession.builder.getOrCreate()

# Llamada sin el parámetro `squeeze`
df_pnd = ps.read_excel(
    "hdfs://192.168.1.137:8020/data/datos_pnd2425-13-05-2025_n.xlsx",
    sheet_name="Indicadores PND24-25",
    header=2  ,       # fila de cabecera,
     dtype=str   
)


num_filas = df_pnd.shape[0]
print(f"Número total de filas: {num_filas}")
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
sdf = df_pnd.to_spark(schema=schema)
sdf.printSchema()
sdf.show(5)