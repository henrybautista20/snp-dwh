#!/bin/bash
docker cp /var/snp-dwh/sftp/sftp-data/datos_pnd2425-13-05-2025_n.xlsx snp-dwh-hadoop-namenode-1:/tmp/datos_pnd2425-13-05-2025_n.xlsx
docker exec snp-dwh-hadoop-namenode-1 hdfs dfs -mkdir -p /data
docker exec snp-dwh-hadoop-namenode-1 hdfs dfs -put -f /tmp/datos_pnd2425-13-05-2025_n.xlsx /data/
rm /var/snp-dwh/sftp/sftp-data/datos_pnd2425-13-05-2025_n.xlsx
