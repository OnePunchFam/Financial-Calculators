
"""

Black-Scholes model for American-style options in Python using the binomial tree method. 
This implementation also assumes that the underlying asset pays no dividends.

"""


import math
from scipy.stats import norm

def american_option(S, K, r, sigma, T, option_type, N):
    """
    Calculates the price of an American option using the Black-Scholes model and the binomial tree method.

    Parameters:
    S (float): current price of the underlying asset
    K (float): strike price of the option
    r (float): risk-free interest rate
    sigma (float): volatility of the underlying asset
    T (float): time to expiration of the option (in years)
    option_type (str): type of the option, either 'call' or 'put'
    N (int): number of steps in the binomial tree

    Returns:
    float: price of the option
    """
    delta_t = T / N
    u = math.exp(sigma * math.sqrt(delta_t))
    d = 1 / u
    p = (math.exp(r * delta_t) - d) / (u - d)

    # Initialize stock prices at expiration
    stock_prices = [S * u**(N - i) * d**i for i in range(N + 1)]

    # Initialize option values at expiration
    option_values = [max(0, K - stock_price) if option_type == 'call' else max(0, stock_price - K) for stock_price in stock_prices]

    # Calculate option values at each node in the tree
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            stock_price = S * u**(i - j) * d**j
            exercise_value = max(0, K - stock_price) if option_type == 'call' else max(0, stock_price - K)
            continuation_value = math.exp(-r * delta_t) * (p * option_values[j] + (1 - p) * option_values[j + 1])
            option_values[j] = max(exercise_value, continuation_value)

    return option_values[0]



"""

This implementation uses the binomial tree method to calculate the option prices at each node in the tree, starting from the expiration date and working backwards to the present. 
At each node, the option value is the maximum of the exercise value and the continuation value. 
The exercise value is the payoff of the option if it were exercised immediately, while the continuation value is the expected value of the option if it were held until the next time step.

"""


S = 100   # current price of the underlying asset
K = 110   # strike price of the option
r = 0.05  # risk-free interest rate
sigma = 0.2  # volatility of the underlying asset
T = 0.5   # time to expiration of the option (in years)
option_type = 'call'  # type of the option
N = 100   # number of steps in the binomial tree

price = american_option(S, K, r, sigma, T, option_type, N)
print(f"The price of the {option_type} option is: {price:.2f}")