FROM ubuntu:latest

# Variables de entorno
ENV JDK_VER=21.0.1
ENV HADOOP_VER=3.3.6
ENV JDK_TAR_NAME=jdk.tar.gz
ENV HADOOP_TAR_NAME=hadoop.tar.gz

# Actualizar e instalar dependencias
RUN apt-get update && \
    apt-get install -y arp-scan python3 openjdk-8-jre && \
    rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /opt

# Agregar y descomprimir archivos tar de Java y Hadoop
ADD ./assets/${JDK_TAR_NAME} .
ADD ./assets/${HADOOP_TAR_NAME} .
RUN ls 

# Configuración de Java en el PATH
ENV JAVA_HOME /opt/jdk-${JDK_VER}
ENV PATH $PATH:$JAVA_HOME/bin

# Configuración de Hadoop en el PATH
ENV HADOOP_HOME /opt/hadoop-${HADOOP_VER}
ENV PATH $PATH:$HADOOP_HOME/bin

# Descargar y configurar las bibliotecas de JAXB manualmente
RUN apt-get install -y wget && \
    wget https://repo1.maven.org/maven2/javax/xml/bind/jaxb-api/2.3.1/jaxb-api-2.3.1.jar -P /opt && \
    wget https://repo1.maven.org/maven2/com/sun/xml/bind/jaxb-impl/2.3.0.1/jaxb-impl-2.3.0.1.jar -P /opt && \
    wget https://repo1.maven.org/maven2/com/sun/xml/bind/jaxb-core/2.3.0.1/jaxb-core-2.3.0.1.jar -P /opt
# Agregar archivos de configuración de Hadoop
ADD ./config-files/hadoop-env.sh $HADOOP_HOME/etc/hadoop/
ADD ./config-files/core-site.xml $HADOOP_HOME/etc/hadoop/
