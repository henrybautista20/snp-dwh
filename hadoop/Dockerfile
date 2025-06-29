root@SNP-DWH:/var/snp-dwh/hadoop# cat Dockerfile
FROM openjdk:11-jre-slim

ENV HADOOP_VERSION=3.3.1
ENV HADOOP_HOME=/opt/hadoop-${HADOOP_VERSION}
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

RUN apt-get update && apt-get install -y --no-install-recommends openssh-server rsync wget

RUN useradd -m hadoop

RUN mkdir -p $HADOOP_HOME /log /hadoop/hdfs/namenode /hadoop/hdfs/datanode && \
    chown -R hadoop:hadoop $HADOOP_HOME /log /hadoop

WORKDIR $HADOOP_HOME

RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz --strip-components=1 && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

COPY config $HADOOP_HOME/etc/hadoop

EXPOSE 9000 9870 8088

USER hadoop

ENTRYPOINT ["/bin/bash", "-c", "hdfs namenode -format -nonInteractive -force && start-dfs.sh && start-yarn.sh && tail -f /log/hadoop-hdfs-namenode.log"]