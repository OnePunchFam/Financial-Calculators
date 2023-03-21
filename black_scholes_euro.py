"""

BSM: Assume that the underlying asset pays no dividends, and that the option is of the European type.

"""



import math
from scipy.stats import norm

def black_scholes(S, K, r, sigma, T, option_type):
    """
    Calculates the price of a European option using the Black-Scholes model.

    Parameters:
    S (float): current price of the underlying asset
    K (float): strike price of the option
    r (float): risk-free interest rate
    sigma (float): volatility of the underlying asset
    T (float): time to expiration of the option (in years)
    option_type (str): type of the option, either 'call' or 'put'

    Returns:
    float: price of the option
    """
    d1 = (math.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return price



"""

This implementation uses the math module to perform basic mathematical operations, and the norm method from the scipy.stats module 
to compute the cumulative distribution function (CDF) of the standard normal distribution. 
The CDF is used to calculate the probabilities of the option being in the money or out of the money.

"""


S = 100   # current price of the underlying asset
K = 110   # strike price of the option
r = 0.05  # risk-free interest rate
sigma = 0.2  # volatility of the underlying asset
T = 0.5   # time to expiration of the option (in years)
option_type = 'call'  # type of the option

price = black_scholes(S, K, r, sigma, T, option_type)
print(f"The price of the {option_type} option is: {price:.2f}")