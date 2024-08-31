from statsmodels.tsa.ardl import ARDL
import setup

# ARDL Model with lags of Y and X
def ardl_model(Y, X, p=1, q=1):
    model = ARDL(Y, X, lags=(p, q))
    result = model.fit()
    return result

# Test different ARDL models
ardl_results = {}
for p in range(1, 4):
    for q in range(1, 4):
        ardl_results[f'ARDL({p},{q})'] = ardl_model(setup.stock_prices, setup.investor_sentiment, p, q)

for model_name, result in ardl_results.items():
    print(f"{model_name} - AIC: {result.aic:.4f}, BIC: {result.bic:.4f}")
