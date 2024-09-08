import numpy as np
from scipy.stats import binom
from scipy.optimize import minimize 
import generateSample as gp

# Maximum Likelihood Estimation (MLE)
def binomial_log_likelihood(params, data):
    n, p = params
    # Log likelihood for binomial distribution
    return -np.sum(binom.logpmf(data, int(n), p))

initial_guess = [50, 0.5]  # Initial guess for MLE
mle_result = minimize(binomial_log_likelihood, initial_guess, args=(gp.data,))
mle_n, mle_p = mle_result.x
print(f"MLE Estimation - n: {mle_n:.3f}, p: {mle_p:.3f}")

# Step 4b: Method of Moments (MOM)
sample_mean = np.mean(gp.data)
sample_var = np.var(gp.data)

# Moment equations for Binomial (mean = n*p, variance = n*p*(1-p))
def moment_equations(params):
    n, p = params
    mean_eq = sample_mean - n * p
    var_eq = sample_var - n * p * (1 - p)
    return [mean_eq, var_eq]