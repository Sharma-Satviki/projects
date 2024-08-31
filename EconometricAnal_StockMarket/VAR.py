# Fit VAR Model
import setup
model = setup.VAR(setup.data[['Stock_Prices', 'Investor_Sentiment']].dropna())
var_result = model.fit(maxlags=3)

# Summary of VAR model
print(var_result.summary())
