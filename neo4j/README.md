# Neo4j Graph Database Setup for Stock Sentiment Analysis

## Introduction

In this project, Neo4j serves as a critical component in our agentic RAG (Retrieval-Augmented Generation) system, handling stock news data with sentiment analysis. Leveraging Neo4j’s graph database capabilities, we can efficiently store and query complex relationships between companies, news articles, and sentiment scores, offering nuanced insights into public sentiment trends for each stock.

### What is a Graph Database?

A **Graph Database** organizes data in a graph structure consisting of nodes, edges, and properties, making it ideal for relationship-based data:
- **Nodes** represent entities (e.g., companies or news articles).
- **Edges** define the relationships between nodes (e.g., a news article related to a company).
- **Properties** store attributes of nodes and edges (e.g., sentiment of a news article).

Graph databases are especially useful when connections and relationships between data points are essential to the analysis, as in our case with stock sentiment data.

### Why Neo4j for Our Use Case?

**Neo4j** is a leading graph database that uses the property graph model, optimized for queries where relationships are at the forefront. Neo4j’s **Cypher query language** is powerful yet intuitive, allowing us to easily traverse relationships between companies, news articles, and sentiment data. For our RAG system, Neo4j enables us to:

- **Store and Access Complex Relationships**: By storing sentiment-tagged news articles and linking them to corresponding companies, Neo4j allows us to query not just the data itself, but also the relational context.
- **Support Sentiment-Based Insights**: With Neo4j, our system can efficiently retrieve articles associated with each company and assess sentiment trends, aiding in sentiment-aware stock advice.

## Docker Setup for Neo4j

This project uses a Docker container to run a Neo4j instance, simplifying setup and deployment.

### Prerequisites

Ensure Docker is installed on your machine.

### Docker Setup Instructions

1. **Create Local Directories** for data persistence (optional but recommended):
    ```bash
    mkdir -p ~/neo4j/data ~/neo4j/logs ~/neo4j/import ~/neo4j/plugins
    ```

2. **Build the Docker Image**:
    ```bash
    docker build -t my_neo4j .
    ```

3. **Run the Neo4j Container**:
    ```bash
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
   - `-d`: Runs the container in detached mode.
   - `--name neo4j_container`: Names the container `neo4j_container`.
   - `-p 7474:7474` and `-p 7687:7687`: Maps Neo4j’s HTTP and Bolt ports to your host machine.
   - `-v ~/neo4j/...`: Binds the specified local directories to the container, ensuring data persistence.

4. **Access the Neo4j Database**:
    - Open your browser and go to [http://localhost:7474](http://localhost:7474).
    - Log in using the default credentials (set in the Docker setup or `Dockerfile`).

## Data Insertion

The news dataset, including sentiment-tagged articles, is imported into Neo4j with the following structure:

- **Company Node**: Represents individual companies (e.g., `AAPL` for Apple).
- **NewsArticle Node**: Contains details of each news article (e.g., title, date, and link).
- **Sentiment Node**: Represents sentiment types (e.g., positive, neutral, negative).

## Data Structure

In our Neo4j setup, we model stock news articles and sentiment data using a graph structure that includes `Company`, `NewsArticle`, and `Sentiment` nodes. This design enables efficient traversal and querying of relationships, allowing us to analyze sentiment trends for each company based on recent news.

### Nodes

1. **Company Node**:
   - Represents each unique company, identified by its stock ticker symbol (e.g., `AAPL` for Apple, `TSLA` for Tesla).
   - **Properties**:
     - `name` (String): The ticker symbol of the company, which serves as the unique identifier for this node.

2. **NewsArticle Node**:
   - Represents each individual news article related to a company.
   - **Properties**:
     - `title` (String): The title of the news article, used to identify the content of the article.
     - `date` (Date): The publication date of the news article, allowing for time-based filtering.
     - `link` (String): The URL link to the original news article, enabling reference back to the source.
     - `sentiment` (String): The sentiment score or label (e.g., `positive`, `neutral`, `negative`) as analyzed from the article’s content. This property provides a direct view of the public mood around the time of publication.

3. **Sentiment Node**:
   - Represents different sentiment types that can be assigned to a news article (e.g., `positive`, `neutral`, `negative`).
   - **Properties**:
     - `type` (String): The label for sentiment, such as `positive`, `neutral`, or `negative`, which categorizes the sentiment derived from each news article.

### Relationships

1. **RELATED_TO** (between `NewsArticle` and `Company`):
   - **Purpose**: Connects each `NewsArticle` node to the corresponding `Company` node that the article is about.
   - **Example**: If a news article titled “Apple’s Stock Soars” is about Apple, there will be a `RELATED_TO` relationship linking the `NewsArticle` node representing that article to the `Company` node with `name: "AAPL"`.
   - **Use Case**: This relationship allows for quick retrieval of all news articles associated with a specific company, which is essential for sentiment and trend analysis over time.

2. **HAS_SENTIMENT** (between `NewsArticle` and `Sentiment`):
   - **Purpose**: Links each `NewsArticle` node to a specific `Sentiment` node that categorizes the mood of the article.
   - **Example**: An article with a `sentiment` of `positive` would have a `HAS_SENTIMENT` relationship to a `Sentiment` node where `type: "positive"`.
   - **Use Case**: This relationship simplifies sentiment-based queries. By traversing this relationship, we can identify articles with particular sentiment labels, helping us track public opinion trends for specific companies or the overall market.

### Example Data Structure in Neo4j

Imagine we have an article titled “Tesla Reaches New Heights” published on 2023-01-15, marked as `positive` sentiment, and linked to the ticker `TSLA`. This data would be represented as follows:

- **Nodes**:
  - `Company` node: `{ name: "TSLA" }`
  - `NewsArticle` node: `{ title: "Tesla Reaches New Heights", date: "2023-01-15", link: "https://example.com/article", sentiment: "positive" }`
  - `Sentiment` node: `{ type: "positive" }`

- **Relationships**:
  - `(NewsArticle)-[:RELATED_TO]->(Company)`: Links the `NewsArticle` titled “Tesla Reaches New Heights” to the `Company` node `TSLA`.
  - `(NewsArticle)-[:HAS_SENTIMENT]->(Sentiment)`: Links the same `NewsArticle` to a `Sentiment` node labeled as `positive`.


### Data Retrieval

For querying sentiment or relationship-based data, we retrieve nodes and relationships using Cypher queries. For example, our RAG system dynamically translates user inputs into Cypher queries to extract relevant sentiment insights about a specific stock.

