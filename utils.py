import pandas as pd
import pymysql
from config import llm, mysql_conn, neo4j_driver

def load_ticker_mapping(csv_path="../pre-analysis/datasets/stock_name_ticker.csv"):
    try:
        df = pd.read_csv(csv_path)
        return dict(zip(df["company_name"].str.lower(), df["ticker"]))
    except Exception as e:
        print(f"Error loading ticker mapping: {e}")
        return {}

def get_ticker_from_name(company_name, ticker_mapping):
    return ticker_mapping.get(company_name.lower(), None)

def execute_mysql_query(query):
    try:
        with mysql_conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    except pymysql.MySQLError as e:
        return f"MySQL error: {e}"

def execute_neo4j_query(query):
    try:
        with neo4j_driver.session() as session:
            result = session.run(query)
            return [record.data() for record in result]
    except Exception as e:
        return f"Neo4j error: {e}"