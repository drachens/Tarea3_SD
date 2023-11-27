FROM hadoop_base:1

RUN mkdir /opt/hdfs
RUN mkdir /opt/hdfs/namenode

ADD ./config-files/hdfs-site.xml $HADOOP_HOME/etc/hadoop/

RUN hdfs namenode -format
CMD hdfs namenode