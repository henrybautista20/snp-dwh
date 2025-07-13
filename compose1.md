```
docker compose --profile node1 up -d --build
 docker compose --profile node1 down -v

 docker compose --profile node2 up -d --build
 docker compose --profile node1 down -v
---
docker exec -it snp-dwh-airflow-webserver-1 airflow db init && docker exec -it snp-dwh-airflow-scheduler-1 airflow db init

docker exec -it snp-dwh-airflow-webserver-1 airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com

docker exec -it snp-dwh-airflow-webserver-1 \
  airflow connections add spark_remote \
    --conn-type spark \
    --conn-host spark://snp-dwh-spark-master-1 \
    --conn-port 7077

docker exec -it snp-dwh-airflow-webserver-1 \
  airflow connections add hadoop_ssh \
    --conn-type ssh \
    --conn-host 192.168.1.137 \
    --conn-login root \
    --conn-password 1234
    