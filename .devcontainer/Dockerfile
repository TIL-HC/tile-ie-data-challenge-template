# Use the standard Microsoft Python dev container
FROM mcr.microsoft.com/devcontainers/python:3.10

# Install OpenJDK-17 (Required for PySpark)
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get clean;

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64
