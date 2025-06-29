import pandas as pd
import fsspec

# Configura el filesystem apuntando a WebHDFS en el Namenode
fs = fsspec.filesystem(
    "webhdfs",
    host="192.168.1.137",
    port=9870,
    user="airflow"   # usuario HDFS si aplica
)

# Abre el archivo remoto y pásalo a pandas
with fs.open("/data/datos_pnd2425-13-05-2025_n.xlsx", "rb") as f:
    df = pd.read_excel(f, sheet_name="Indicadores PND24-25")

print(df.head())
