from hdfs import InsecureClient
import pandas as pd
from io import StringIO

# URL de WebHDFS del NameNode
hdfs_url = 'http://localhost:9870'  # O usa la IP de tu contenedor si no funciona localhost
hdfs_path = '/data/usuarios.csv'

# Crear cliente
client = InsecureClient(hdfs_url, user='root')

# Leer archivo como string
with client.read(hdfs_path, encoding='utf-8') as reader:
    file_content = reader.read()

# Cargar en pandas
df = pd.read_csv(StringIO(file_content))

# Mostrar contenido
print(df.head())
