# Use the official Neo4j image from Docker Hub
FROM neo4j:latest

# Set environment variables
ENV NEO4J_AUTH=neo4j/password  
ENV NEO4J_ACCEPT_LICENSE_AGREEMENT=yes
ENV NEO4J_dbms_memory_pagecache_size=1G
ENV NEO4J_dbms_memory_heap_initial__size=512m
ENV NEO4J_dbms_memory_heap_max__size=1G

# Expose necessary ports
EXPOSE 7474 7687

# Create directories for persistent storage
VOLUME /data
VOLUME /logs
VOLUME /var/lib/neo4j/import
VOLUME /plugins
