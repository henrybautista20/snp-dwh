version: '3.8'

services:
  postgres:
    build: ./postgres
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - dev-net

  hadoop-namenode:
    image: bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8
    environment:
      - CLUSTER_NAME=dev-hadoop
    ports:
      - "9870:9870"
    volumes:
      - hadoop_namenode:/hadoop/dfs/name
      - ./sftp/sftp-data:/sftp-data
    networks:
      - dev-net

  hadoop-datanode:
    image: bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8
    environment:
      - CORE_CONF_fs_defaultFS=hdfs://hadoop-namenode:8020
      - CORE_CONF_hadoop_http_staticuser_user=root
      - HDFS_CONF_dfs_replication=1
    volumes:
      - hadoop_datanode:/hadoop/dfs/data
      - ./sftp/sftp-data:/sftp-data
    depends_on:
      - hadoop-namenode
    networks:
      - dev-net

  spark-master:
    build: ./spark
    environment:
      - SPARK_MODE=master
      - SPARK_MASTER_PORT=7077
    ports:
      - "8080:8080"
      - "7077:7077"
    networks:
      - dev-net

  spark-worker:
    build: ./spark
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER_URL=spark://spark-master:7077
    depends_on:
      - spark-master
    ports:
      - "8081:8081"
    networks:
      - dev-net

  airflow-webserver:
    build: ./airflow
    environment:
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor
      - AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
      - AIRFLOW__CORE__FERNET_KEY=k8Qb1kQ8w7Qw8h1v2nQw8h1v2nQw8h1v2nQw8h1v2nQw8h1v2nQw8h1v2nQ=
      - AIRFLOW__CORE__LOAD_EXAMPLES=True
      - AIRFLOW__DATABASE__SQL_ALCHEMY_POOL_ENABLED=False
    depends_on:
      - postgres
    ports:
      - "8082:8080"
    user: root  
    volumes:
      - ./airflow/dags:/opt/airflow/dags
      - airflow_logs:/opt/airflow/logs
      - ./spark_jobs:/opt/airflow/spark_jobs
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      - dev-net
    command: webserver

  airflow-scheduler:
    build: ./airflow
    environment:
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor
      - AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
      - AIRFLOW__CORE__FERNET_KEY=k8Qb1kQ8w7Qw8h1v2nQw8h1v2nQw8h1v2nQw8h1v2nQw8h1v2nQw8h1v2nQ=
      - AIRFLOW__CORE__LOAD_EXAMPLES=True
      - AIRFLOW__DATABASE__SQL_ALCHEMY_POOL_ENABLED=False
    depends_on:
      - postgres
      - airflow-webserver
    user: root  
    volumes:
      - ./airflow/dags:/opt/airflow/dags
      - airflow_logs:/opt/airflow/logs
      - ./spark_jobs:/opt/airflow/spark_jobs
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      - dev-net
    command: scheduler

  sftp:
    image: atmoz/sftp
    ports:
      - "2222:22"
    volumes:
      - /var/snp-dwh/sftp/sftp-data:/home/urbadigital/upload
    networks:
      - dev-net
    command: urbadigital:password:1001

networks:
  dev-net:

volumes:
  postgres_data:
  hadoop_namenode:
  hadoop_datanode:
  airflow_logs:
