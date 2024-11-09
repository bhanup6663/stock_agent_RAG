# MySQL Database Setup for Historical Stock Data

## Introduction

In this project, MySQL is used to store and manage historical stock data, enabling efficient retrieval and processing of stock performance data over time. By using MySQL, we ensure reliable storage and support for SQL-based queries, essential for analyzing large volumes of historical stock records.

### Why MySQL for Our Use Case?

**MySQL** is a robust relational database system well-suited for handling structured data. For our RAG system, MySQL provides:

- **Efficient Storage and Retrieval**: MySQL enables efficient handling of historical stock data, with indexing and primary keys that support quick lookups for individual stocks or specific date ranges.
- **SQL Support for Complex Queries**: MySQL allows us to perform complex queries on stock data, such as filtering by date, calculating average values, and aggregating metrics across multiple stocks.

## Docker Setup for MySQL

This project uses a Docker container to run a MySQL instance, making deployment and management simple and consistent across different environments.

### Prerequisites

Ensure Docker is installed on your machine.

### Docker Setup Instructions

1. **Build the Docker Image**:
    ```bash
    docker build -t my_mysql .
    ```

2. **Run the MySQL Container**:
    ```bash
    docker run -d \
      --name mysql_container \
      -e MYSQL_ROOT_PASSWORD=root \
      -e MYSQL_DATABASE=mydatabase \
      -p 3306:3306 \
      my_mysql
    ```
   - `-d`: Runs the container in detached mode.
   - `--name mysql_container`: Names the container `mysql_container`.
   - `-e MYSQL_ROOT_PASSWORD=root`: Sets the root password for MySQL.
   - `-e MYSQL_DATABASE=mydatabase`: Creates a database named `mydatabase` upon container initialization.
   - `-p 3306:3306`: Maps MySQL’s default port to your host machine.

3. **Access the MySQL Database**:
    - You can access MySQL using a client like MySQL Workbench or via command line with the credentials specified in the Docker setup.

## Data Insertion and Structure

The stock data is structured in a table within MySQL with the following schema:

### Stock Data Table (`stock_data`)

- **Schema**:
  - `date` (DATE): The date for the stock entry.
  - `name` (VARCHAR): The ticker symbol of the stock (e.g., `AAPL` for Apple).
  - `open` (FLOAT): The opening price of the stock on the specified date.
  - `high` (FLOAT): The highest price of the stock on the specified date.
  - `low` (FLOAT): The lowest price of the stock on the specified date.
  - `close` (FLOAT): The closing price of the stock on the specified date.
  - `close_adj` (FLOAT): The adjusted closing price, accounting for events like stock splits.
  - `volume` (BIGINT): The total volume of shares traded on the specified date.
  - `source` (VARCHAR): The source of the stock data (e.g., `Yahoo Finance`).

- **Primary Key**: `(date, name)`: A composite primary key ensures that each stock’s entry is unique per date.

### Example Data Structure in MySQL

Consider the following entry for Apple (AAPL) on January 3, 2023:

- **Example Entry**:
  - `date`: `2023-01-03`
  - `name`: `AAPL`
  - `open`: `130.00`
  - `high`: `135.00`
  - `low`: `129.00`
  - `close`: `134.00`
  - `close_adj`: `134.00`
  - `volume`: `5000000`
  - `source`: `Yahoo Finance`

This schema allows us to store and retrieve stock data based on dates and stock tickers, making it easy to perform historical analysis or comparisons across multiple stocks.

### Basic Data Retrieval

For querying specific stock data or time ranges, we retrieve records using SQL commands. In our RAG system, user input is dynamically converted into SQL queries to pull relevant historical stock data as needed.
