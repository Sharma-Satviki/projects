import numpy as np
from scipy.stats import binom
from scipy.optimize import minimize # type: ignore

# Step 2: Generate Random Data (Binomial Distribution)
n_true = 100    # true number of trials
p_true = 0.2    # true probability of success
sample_size = 1000
data = binom.rvs(n_true, p_true, size=sample_size)

# Step 3: Create frequency distribution (binning)
num_bins = 10
bin_edges = np.linspace(0, n_true, num_bins + 1)
freq, _ = np.histogram(data, bins=bin_edges)
bin_midpoints = (bin_edges[:-1] + bin_edges[1:]) / 2