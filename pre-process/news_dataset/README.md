# News Data Preprocessing

## Introduction

The dataset consists of news articles related to various stocks from Yahoo Finance News. This data includes article titles, publication dates, and publishers, covering multiple years. Sentiment analysis is applied to enhance insights on public perception regarding different stocks, which is then integrated into the stock analysis pipeline.

This document provides a detailed explanation of the preprocessing techniques applied to ensure data quality and sentiment analysis consistency.

## Key Features

### Yahoo Finance News Data Retrieval
- Retrieves news articles for a comprehensive list of tickers using the `yfinance` API from January 2015 to January 2023.
- The tickers represent leading companies across various sectors.
- Each article includes fields such as `title`, `date`, `publisher`, and `link`.
- Articles are filtered based on publication dates to align with the stock data's timeframe.

## Data Cleaning and Preparation

### Handling Missing Data
- Articles without a title or date are excluded.
- Missing news tickers are logged in `missing_news_tickers.txt` for future reference.

### Text Preprocessing
- The news titles are preprocessed for sentiment analysis by:
  - Lowercasing all text.
  - Removing special characters and punctuation.
  - Tokenizing words and removing stop words.
  - Applying lemmatization to standardize word forms.

### Sentiment Analysis
- Sentiment analysis is performed using the `VADER` SentimentIntensityAnalyzer, which tags each article as `positive`, `neutral`, or `negative`.
- Sentiment scores are stored in the `sentiment` column for each article.

## Data Merging

The cleaned and processed news data is saved in a CSV format (`news_with_sentiment.csv`) for seamless integration with the stock data.

## Initial Observations Before Preprocessing

### 1.1 Missing Data
**Problem**: Some articles lacked publication dates or titles, which are essential for analysis and alignment with stock data.

**Impact**: Missing data points could skew the sentiment distribution and lead to inaccurate insights.

## Preprocessing Techniques

### 2.1 Text Cleaning and Sentiment Analysis
- **Text Cleaning**: The `clean_text` function removes noise, converts text to lowercase, removes stop words, and lemmatizes the words.
- **Sentiment Analysis**: The VADER analyzer scores each article, categorizing them as `positive`, `neutral`, or `negative`, aiding in assessing market sentiment.

## Impact of Preprocessing on the Dataset

### 3.1 Before Preprocessing
- The dataset contained incomplete entries, varying text formats, and unstandardized sentiment cues.

### 3.2 After Preprocessing
- **Sentiment Consistency**: Sentiment labels provide a quick overview of public sentiment.
- **Cleaned Titles**: Standardized titles make sentiment analysis results more reliable.

## Output

The final processed dataset, saved as `news_with_sentiment.csv`, includes:
- `ticker`: Stock ticker symbol
- `title`: Original title of the news article
- `cleaned_title`: Preprocessed title for sentiment analysis
- `publisher`: Source of the article
- `link`: URL link to the article
- `date`: Publication date of the article
- `sentiment`: Sentiment label (positive, neutral, or negative)

This dataset can be used to enhance stock trend predictions by incorporating public sentiment insights.

## Libraries Used

- **yfinance**: For fetching news data programmatically from Yahoo Finance.
- **pandas**: For data cleaning and manipulation.
- **VADER SentimentIntensityAnalyzer**: For sentiment scoring of news titles.
- **nltk**: For text preprocessing, including stop word removal, tokenization, and lemmatization.

## Instructions for Running the Code

1. Clone the repository and ensure all required libraries are installed.
2. Run `fetch_yahoo_finance_news()` to retrieve and save news articles.
3. Execute the sentiment analysis code to process the titles and generate sentiment labels.
4. The final dataset will be saved as `news_with_sentiment.csv`.
