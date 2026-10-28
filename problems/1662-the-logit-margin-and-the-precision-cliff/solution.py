import numpy as np


def logit_margin(z, t):
    """Margin m = z_t - log sum_{j != t} exp(z_j), computed stably; returns a Python float."""
    z_other = np.delete(z,t)
    mx = np.max(z_other)

    log_sum = np.log(np.sum(np.exp(z_other-mx))) + mx

    m = z[t] - log_sum
    return float(m)

    


def precision_cliff(dtype) -> float:
    """Smallest m >= 0 at which 1/(1 + exp(-m)) == 1 when evaluated in dtype; bisection on a float64 m.

    Returns the margin rounded to 4 decimals.
    """
    dt = np.dtype(dtype)
    low = 0.0
    high = 100.0  # Safe upper bound covering float16, float32, and float64
    
    # Bisection search
    for _ in range(100):
        mid = (low + high) / 2.0
        val = dt.type(1.0) / (dt.type(1.0) + dt.type(np.exp(-mid)))
        if val == dt.type(1.0):
            high = mid
        else:
            low = mid
            
    return round(float(high), 4)