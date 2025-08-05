import subprocess
from airflow.sensors.base import BaseSensorOperator
from airflow.utils.decorators import apply_defaults


class HadoopFileSensor(BaseSensorOperator):
    """
    Sensor personalizado que verifica si un archivo existe en HDFS
    ejecutando un comando docker exec dentro del contenedor NameNode.
    """

    @apply_defaults
    def __init__(self, container_name: str, hdfs_path: str, *args, **kwargs):
        super(HadoopFileSensor, self).__init__(*args, **kwargs)
        self.container_name = container_name
        self.hdfs_path = hdfs_path

    def poke(self, context):
        """
        Ejecuta el comando hdfs dfs -test -e <file> en el contenedor.
        Retorna True si el archivo existe, False si no.
        """
        cmd = f"docker exec {self.container_name} hdfs dfs -test -e {self.hdfs_path}"
        self.log.info(f"Verificando existencia de archivo en HDFS: {self.hdfs_path}")

        result = subprocess.call(cmd, shell=True)
        if result == 0:
            self.log.info(f"✅ Archivo encontrado en HDFS: {self.hdfs_path}")
            return True
        else:
            self.log.warning(f"⏳ Archivo no encontrado aún: {self.hdfs_path}")
            return False
