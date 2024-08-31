import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf # type: ignore
import setup

# Plotting ACF and PACF for Stock Prices
def plot_autocorrelation(series, lags=30, title=''):
    fig, ax = plt.subplots(2, figsize=(12,8))
    
    # ACF plot
    plot_acf(series.dropna(), lags=lags, ax=ax[0])
    ax[0].set_title(f'Autocorrelation (ACF) of {title}')
    
    # PACF plot
    plot_pacf(series.dropna(), lags=lags, ax=ax[1])
    ax[1].set_title(f'Partial Autocorrelation (PACF) of {title}')
    
    plt.tight_layout()
    plt.show()

# Plot ACF and PACF for Stock Prices and Investor Sentiment
plot_autocorrelation(setup.stock_prices, lags=30, title='Stock Prices')
plot_autocorrelation(setup.investor_sentiment, lags=30, title='Investor Sentiment')
