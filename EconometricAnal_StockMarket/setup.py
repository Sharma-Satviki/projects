import numpy as np
import pandas as pd
import statsmodels.api as sm # type: ignore
from statsmodels.tsa.stattools import adfuller, coint # type: ignore
from statsmodels.tsa.api import VAR
from statsmodels.tsa.ar_model import AutoReg
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

# Load the data (Assuming the dataset is in CSV format)
data = pd.read_csv('stockMarket_data.csv', parse_dates=['Date'], index_col='Date')

# Separate variables
stock_prices = data['Stock_Prices']
investor_sentiment = data['Investor_Sentiment']
