docker exec -it snp-dwh-spark-master \
bash -c "mkdir -p /opt/bitnami/spark/.ivy2 && HOME=/opt/bitnami/spark spark-submit \
  --master spark://snp-dwh-spark-master:7077 \
  --deploy-mode client \
  --conf spark.jars.ivy=/opt/bitnami/spark/.ivy2 \
  /opt/spark-apps/wordcount.py"
