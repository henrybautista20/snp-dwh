#!/bin/bash
docker cp /var/snp-dwh/sftp/sftp-data/usuarios.csv snp-dwh-hadoop-namenode-1:/tmp/usuarios.csv
docker exec snp-dwh-hadoop-namenode-1 hdfs dfs -mkdir -p /data
docker exec snp-dwh-hadoop-namenode-1 hdfs dfs -put -f /tmp/usuarios.csv /data/
rm /var/snp-dwh/sftp/sftp-data/usuarios.csv