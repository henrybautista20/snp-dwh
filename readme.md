
# Guía rápida para inicializar Airflow + Spark + PostgreSQL

## 🔑 1. Generar la clave Fernet
Airflow necesita una clave Fernet para cifrar datos sensibles.

```bash
python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

> Copia el resultado y configúralo en tu `docker-compose.yml` bajo:
>
> ```yaml
> environment:
>   - AIRFLOW__CORE__FERNET_KEY=<tu_clave_aqui>
> ```

---
corre
```
> docker compose up -d 
---


```
## 🚀 2. Levantar los servicios principales

```
bash
docker compose up -d airflow-webserver airflow-scheduler
```

---

## 🗄 3. Inicializar la base de datos de Airflow

```bash
docker exec -it snp-dwh-airflow-webserver airflow db init && docker exec -it snp-dwh-airflow-scheduler airflow db init
```
docker compose --profile node1 up -d --build
 docker compose --profile node1 down -v
---

docker exec -u root -it snp-dwh-spark-1 bash


## 👤 4. Crear el usuario administrador de Airflow

```bash
docker exec -it snp-dwh-airflow-webserver airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com
```
docker compose --profile node2 up -d --build
docker compose --profile node2 down -v
---
docker exec -u root -it snp-dwh-spark-master-1 bash

## 🔗 5. Crear la conexión a Spark

Crea la conexión `spark_remote` apuntando a tu master Spark en `spark://snp-dwh-spark-master-1:7077`:

```bash
docker exec -it snp-dwh-airflow-webserver \
  airflow connections add spark_remote \
    --conn-type spark \
    --conn-host spark://snp-dwh-spark-master \
    --conn-port 7077

docker exec -it snp-dwh-airflow-webserver \
  airflow connections add hadoop_ssh \
    --conn-type ssh \
    --conn-host 127.0.0.1 \
    --conn-login root \
    --conn-password 1234
```
docker exec -it snp-dwh-airflow-webserver-1 
---

## 📥 6. Descargar el driver JDBC de PostgreSQL

```bash
wget https://jdbc.postgresql.org/download/postgresql-42.7.3.jar
```

---

## 📁 7. Copiar el driver JDBC a los contenedores de Airflow

Crear directorios en los contenedores:

```bash
docker exec -it snp-dwh-airflow-webserver-1 bash -c "mkdir -p /opt/airflow/jars"
docker exec -it snp-dwh-airflow-scheduler-1 bash -c "mkdir -p /opt/airflow/jars"
```

Copiar el driver:

```bash
docker cp postgresql-42.7.3.jar snp-dwh-airflow-webserver-1:/opt/airflow/jars/postgresql-42.7.3.jar
docker cp postgresql-42.7.3.jar snp-dwh-airflow-scheduler-1:/opt/airflow/jars/postgresql-42.7.3.jar
```

---

## ☕ 8. Instalar Java en tu máquina local (opcional para Spark local)

```bash
apt update \
  && apt install -y --no-install-recommends openjdk-17-jdk-headless ant \
  && ln -sfn /usr/lib/jvm/java-17-openjdk-amd64 /usr/lib/jvm/java-17-openjdk-arm64 \
  && apt clean \
  && rm -rf /var/lib/apt/lists/*
```

Configurar el `JAVA_HOME`:

```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
```

Puedes agregarlo a tu `~/.bashrc` para que quede permanente:

```bash
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
source ~/.bashrc
```

---

✅ **¡Listo!**  
Con esto tu entorno Airflow está inicializado, tiene la conexión a Spark y puede comunicarse con PostgreSQL mediante el driver JDBC.
