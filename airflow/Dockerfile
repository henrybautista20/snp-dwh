FROM apache/airflow:2.9.1

# Switch to root to install OS packages
USER root

# Update package lists, install Java 17 and Ant, create a symlink for the expected ARM64 path,
# then clean up to reduce image size
RUN apt update \
    && apt install -y --no-install-recommends openjdk-17-jdk-headless ant \
    && ln -sfn /usr/lib/jvm/java-17-openjdk-amd64 /usr/lib/jvm/java-17-openjdk-arm64 \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Define JAVA_HOME pointing to the correct AMD64 directory
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Switch back to the airflow user
USER airflow

# Reinstall psycopg2 for Postgres
RUN pip install --no-cache-dir \
      psycopg2-binary \
      pyspark==3.5.6 \
      apache-airflow-providers-apache-spark==4.1.1

