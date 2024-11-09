# Pre-Process

## Overview

The `pre-process` folder is central to the development of our agentic RAG (Retrieval-Augmented Generation) system, designed to assist users with insights on stock performance and sentiment-based recommendations. To make reliable predictions, we rely on two critical datasets:

1. **Stock Dataset**: This dataset provides historical stock prices and trading volumes, essential for understanding performance trends across various companies.
2. **News Dataset**: This dataset contains news articles with sentiment analysis, helping to gauge public perception around each stock.

Together, these datasets enable our RAG system to advise on market trends and sentiment, offering more informed perspectives for stock decision-making.

## Datasets

### [Stock Dataset](https://github.com/bhanup6663/stock_agent_RAG/tree/main/pre-process/stocks_dataset)

The stock data includes historical records of stock prices, collected from multiple sources. It contains features such as open, high, low, close prices, volume, and adjusted close prices. The processed data is structured to support time series analysis and can be used to predict future trends in stock performance. See the [Stock Dataset README](https://github.com/bhanup6663/stock_agent_RAG/tree/main/pre-process/stocks_dataset) for detailed information on data sources, cleaning, and preprocessing techniques.

### [News Dataset](https://github.com/bhanup6663/stock_agent_RAG/tree/main/pre-process/news_dataset)

The news dataset comprises sentiment-analyzed articles, collected from Yahoo Finance News, covering multiple years and companies. Each article is preprocessed to remove noise and then analyzed to produce sentiment scores, which reflect the public mood toward specific stocks. This sentiment data adds a valuable perspective when evaluating stock trends. For detailed steps on the data retrieval and preprocessing, please see the [News Dataset README](https://github.com/bhanup6663/stock_agent_RAG/tree/main/pre-process/news_dataset).

## Purpose of the Pre-Processing

The stock and news datasets are preprocessed to ensure data quality and compatibility with the RAG system’s requirements. By standardizing, cleaning, and analyzing the data beforehand, we make it ready for training predictive models and generating accurate, sentiment-aware recommendations for stock market insights.
