docker exec -it snp-dwh-postgres-1 psql -U airflow -c "CREATE DATABASE usuario_db;"


docker exec -it snp-dwh-airflow-webserver-1  airflow dags list

wget -q https://repo1.maven.org/maven2/com/crealytics/spark-excel_2.12/0.13.7/spark-excel_2.12-0.13.7.jar   # :contentReference[oaicite:0]{index=0}
wget -q https://repo1.maven.org/maven2/org/apache/poi/poi/4.1.2/poi-4.1.2.jar                           # :contentReference[oaicite:1]{index=1}
wget -q https://repo1.maven.org/maven2/org/apache/poi/poi-ooxml/4.1.2/poi-ooxml-4.1.2.jar               # :contentReference[oaicite:2]{index=2}
wget -q https://repo1.maven.org/maven2/org/apache/xmlbeans/xmlbeans/3.1.0/xmlbeans-3.1.0.jar           # :contentReference[oaicite:3]{index=3}
wget -q https://repo.maven.apache.org/maven2/org/apache/commons/commons-math3/3.6.1/commons-math3-3.6.1.jar # :contentReference[oaicite:4]{index=4}
wget -q https://repo1.maven.org/maven2/org/apache/poi/ooxml-schemas/1.4/ooxml-schemas-1.4.jar           # :contentReference[oaicite:5]{index=5}
wget -q https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.3/postgresql-42.7.3.jar

Cambios en el Dag
1. los las rutas
2. airflow user root
3. jars add
4. crear base de datos
5. permitir a hadoopp ver sftp
6. add docker file 