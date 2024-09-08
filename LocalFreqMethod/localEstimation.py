import numpy as np
from scipy.stats import binom
from scipy.optimize import minimize 
import generateSample as gp

def lfr_estimation(freq, midpoints):
    # Take the top 3 frequencies and corresponding midpoints
    f1, f2, f3 = freq[:3]
    x1, x2, x3 = midpoints[:3]
    f12 = f1 / f2
    f23 = f2 / f3

    # Define equations to estimate n and p
    def equations(params):
        n, p = params
        # Approximate binomial probabilities for these midpoints
        prob1 = binom.pmf(round(x1), int(n), p)
        prob2 = binom.pmf(round(x2), int(n), p)
        prob3 = binom.pmf(round(x3), int(n), p)
        eq1 = prob1 / prob2 - f12
        eq2 = prob2 / prob3 - f23
        return [eq1, eq2]

    result = minimize(lambda params: sum(np.square(equations(params))), gp.initial_guess)
    return result.x

lfr_n, lfr_p = lfr_estimation(gp.freq, gp.bin_midpoints)
print(f"LFR Estimation - n: {lfr_n:.3f}, p: {lfr_p:.3f}")
