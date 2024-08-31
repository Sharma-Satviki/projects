# ADF Test
import setup

def adf_test(series, name=''):
    result = adfuller(series.dropna())
    print(f'{name} ADF Statistic: {result[0]:.4f}, p-value: {result[1]:.4f}')
    return result

adf_test(setup.stock_prices, 'Stock Prices')
adf_test(setup.investor_sentiment, 'Investor Sentiment')