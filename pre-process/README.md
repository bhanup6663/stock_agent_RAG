# README: Stock Data Preprocessing and Integration for Time Series Modeling

## Introduction

The dataset we are working with consists of stock prices and trading volumes across multiple stocks, including features such as open, high, low, close, adj_close, and volume. The dataset spans multiple years and contains millions of entries. Before training any time series models (such as LSTMs), it was crucial to improve the quality of the dataset by performing data preprocessing steps, including handling outliers, normalizing data, and dealing with missing values.

This report provides a detailed explanation of the preprocessing techniques applied to ensure the quality of the dataset and the integration of data from different sources: Yahoo Finance, S&P 500, and Tesla stock data.

## Key Features

### Yahoo Finance Data Integration
- Retrieves stock data for a wide range of companies using the `yfinance` API for the period from January 2015 to January 2023.
- The list of tickers includes prominent companies across multiple industries.
- The fetched data includes open, high, low, close, adjusted close, and volume for each company.
- The data is structured and stacked into a clean format with renamed columns and an additional `source` column to specify the data origin as Yahoo Finance.

### S&P 500 Data Integration
- Loads historical stock data from a local CSV file.
- Cleans the dataset by dropping rows with missing values.
- Adds a `source` column to distinguish this dataset from others.

### Tesla Data Integration
- Loads Tesla's historical stock data from a CSV file sourced from Kaggle.
- Adds a `source` column and assigns the company name as 'Tesla' for consistent identification in the combined dataset.

## Data Cleaning and Preparation

### Column Renaming
- Consistent column names across all datasets to facilitate easy merging. Column names such as `open`, `high`, `low`, `close`, `adj_close`, and `volume` are standardized.

### Date Formatting
- Ensures that date columns are uniformly formatted across all datasets to enable accurate time-based analysis. The date values are converted to `datetime` objects and are cleaned to contain only the date part.

### Adjusting Data Fields
- For the S&P 500 data, `adj_close` values are set to missing (`NA`) as they are not present in the original data source.

## Data Merging

The cleaned datasets are concatenated into a single DataFrame using Pandas. The combined data includes:

- Yahoo Finance data for multiple companies.
- S&P 500 stock data.
- Tesla stock data.

After merging, the combined dataset contains the following fields for each stock entry:
- Date
- Open
- High
- Low
- Close
- Adjusted Close (where applicable)
- Volume
- Stock Name (or Ticker)
- Source (Yahoo Finance, SP500, or Kaggle for Tesla)

## Initial Observations Before Preprocessing

### 1.1 Outliers
**Problem**: Extreme values (outliers) were observed in the volume feature, with volumes ranging from zero to billions of shares. This suggested the presence of highly volatile stocks or erroneous data entries.

**Impact**: Outliers skew the model’s understanding of data distribution, which could lead to poor generalization. Extreme volume values could dominate the model's learning and cause overfitting.

### 1.2 Missing or Erroneous Data
**Problem**: Missing and erroneous data, particularly in the `adj_close` column, were detected. Some negative values were present, which are erroneous since adjusted close prices cannot be negative.

**Impact**: Missing or incorrect data introduces noise into the model training process, disrupting the continuity necessary for time series models like LSTMs.

### 1.3 Data Range and Variability
**Problem**: Large variability was noted across different features, such as stock prices ranging from a few cents to over $2,500, and trading volumes ranging from 0 to over 3 billion.

**Impact**: Large feature ranges complicate learning for models like LSTMs, as features with large values (such as volume) may dominate training while smaller features (such as stock prices) are neglected.

## Preprocessing Techniques

### 2.1 Outlier Handling (Capping)
**Technique Used**: Capping was applied at the 99th percentile for the volume feature to reduce the influence of extreme values without losing valuable high-volume instances.

**Effect on Data**: The volume distribution became more balanced, reducing skew and enabling better model generalization.

### 2.2 Normalization (Min-Max Scaling)
**Technique Used**: Min-Max scaling was applied to normalize price-related features and volume to a range between 0 and 1.

**Effect on Data**: This ensured that all features are on the same scale, preventing larger-valued features from dominating the learning process. It also preserved the relationships between stock prices, crucial for time series analysis.

### 2.3 Handling Missing/Erroneous Data
**Technique Used**: Forward fill was used to impute missing values in the dataset, ensuring that no data gaps existed.

**Effect on Data**: The forward fill method maintained the continuity of the time series, which is crucial for LSTM models to learn effectively from sequential data.

## Impact of Preprocessing on the Dataset

### 3.1 Before Preprocessing
- The dataset contained extreme outliers, large variability in feature ranges, and missing/erroneous values, all of which would have negatively impacted model training.
- The presence of large differences between features (e.g., prices vs. volumes) could lead to poor model convergence and inaccurate predictions.

### 3.2 After Preprocessing
- **Outlier Impact**: By capping extreme values, we reduced the influence of rare, extreme trading days, making the dataset more uniform and easier for the model to interpret.
- **Normalization Impact**: Scaling the features between 0 and 1 ensured that the model would treat all features equally, preventing any single feature from dominating the learning process. This also helps the model converge more quickly and learn more effectively.
- **Missing Data Impact**: Forward filling ensured that there were no gaps in the dataset, maintaining the continuity necessary for time series models like LSTMs.

## Output

The final combined dataset was saved as a CSV file (`sp500_data_with_index.csv`). This dataset includes:
- Date
- Open, high, low, close, adj_close
- Volume
- Stock Name (or Ticker)
- Data Source

This consolidated dataset can be used for training time series models, such as LSTMs, to predict stock prices and other market movements.

## Libraries Used

- **yfinance**: For fetching stock data programmatically from Yahoo Finance.
- **pandas**: For data cleaning, manipulation, and integration.
- **datetime**: For handling date formats in the dataset. 

## Instructions for Running the Code

1. Clone the repository and ensure the required libraries are installed.
2. Fetch the Yahoo Finance data programmatically using the provided `yfinance` implementation.
3. Load the S&P 500 and Tesla datasets from the appropriate CSV files.
4. After merging and preprocessing, the final dataset will be saved as `sp500_data_with_index.csv`.
