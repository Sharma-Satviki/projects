import pandas as pd
import setup
def finite_distributed_lag_model(Y, X, max_lag=3):
    results = {}
    for lag in range(1, max_lag + 1):
        # Add lagged terms
        X_lagged = pd.concat([X.shift(i) for i in range(lag+1)], axis=1).dropna()
        Y_lagged = Y.loc[X_lagged.index]
        
        # Run OLS regression
        model = setup.sm.OLS(Y_lagged, setup.sm.add_constant(X_lagged))
        result = model.fit()
        results[f'FDL with {lag} lag(s)'] = result
    
    return results

fdl_results = finite_distributed_lag_model(setup.stock_prices, setup.investor_sentiment)
for model_name, result in fdl_results.items():
    print(f"{model_name} - R-squared: {result.rsquared:.4f}, AIC: {result.aic:.4f}, BIC: {result.bic:.4f}")