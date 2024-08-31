# Test for Cointegration

import setup
def test_cointegration(Y, X):
    score, p_value, _ = setup.coint(Y, X)
    print(f"Cointegration test - p-value: {p_value:.4f}")
    
test_cointegration(setup.stock_prices, setup.investor_sentiment)
