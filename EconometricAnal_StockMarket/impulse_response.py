# Impulse Response Function
import setup
irf = setup.var_result.irf(10)
irf.plot(orth=False)

# Variance Decomposition
fevd = setup.var_result.fevd(10)
fevd.plot(figsize=(10, 6))
