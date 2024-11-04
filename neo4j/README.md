# Neo4j Graph Database in Docker

## Introduction

### What is a Graph Database?
A **Graph Database** is a type of NoSQL database that represents data in a graph structure with nodes, edges, and properties. In graph databases:
- **Nodes** represent entities (such as people, places, items).
- **Edges** represent relationships between these entities (such as "friends with" or "bought by").
- **Properties** store information about both nodes and edges (like a person’s name or a purchase date).

Graph databases are optimized for traversing relationships between entities, making them ideal for applications where relationships and connections between data points are central, like social networks, recommendation engines, fraud detection, and network analysis.

### What is Neo4j?
**Neo4j** is a leading graph database management system that uses the property graph model. It’s highly performant for complex queries and relationship-heavy data. Neo4j supports the **Cypher query language**, designed specifically for working with graphs, allowing users to write expressive, readable, and efficient queries.

Neo4j is available as both a standalone software and as a Docker container, allowing for easy setup and scalability in environments where containerization is preferred.

## Docker Setup

This project uses a `Dockerfile` to set up and run a Neo4j instance within a Docker container. This setup allows you to quickly deploy a Neo4j database without having to install Neo4j manually on your system.

### Dockerfile Explanation

The `Dockerfile` included in this directory contains configuration settings to customize Neo4j. 

## How to Run the Neo4j Docker Container

### Prerequisites

Ensure that Docker Desktop is installed on your machine.

### Steps to Run

1. **Create Local Directories** for data persistence. This step ensures that your Neo4j data, logs, and other files are stored locally on your machine(optional):

```
mkdir -p ~/neo4j/data ~/neo4j/logs ~/neo4j/import ~/neo4j/plugins
```

2. **Build the Docker Image**:
```
docker build -t my_neo4j .
```

3. **Run the Neo4j Container**:
```
docker run -d \
  --name neo4j_container \
  -p 7474:7474 \
  -p 7687:7687 \
  -v ~/neo4j/data:/data \
  -v ~/neo4j/logs:/logs \
  -v ~/neo4j/import:/var/lib/neo4j/import \
  -v ~/neo4j/plugins:/plugins \
  my_neo4j
```
- -d: Runs the container in detached mode.
- --name neo4j_container: Names the container neo4j_container.
- -p 7474:7474 and -p 7687:7687: Maps the Neo4j HTTP and Bolt ports to your host machine.
- -v ~/neo4j/...: Binds the specified local directories to the container, ensuring data persists.

4. **Access the Neo4j Database**:
- Open your web browser and navigate to http://localhost:7474.
- Log in with the username neo4j and the password you set in the Dockerfile.

