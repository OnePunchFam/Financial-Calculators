"""

Implementation of the Black-Scholes model for American-style options in Python, taking dividends into account using the binomial tree method.

"""


import math
from scipy.stats import norm

def american_option(S, K, r, sigma, T, option_type, N, div_yield=0.0, div_dates=[], div_amounts=[]):
    """
    Calculates the price of an American option using the Black-Scholes model and the binomial tree method, taking into account
    the effect of dividends.

    Parameters:
    S (float): current price of the underlying asset
    K (float): strike price of the option
    r (float): risk-free interest rate
    sigma (float): volatility of the underlying asset
    T (float): time to expiration of the option (in years)
    option_type (str): type of the option, either 'call' or 'put'
    N (int): number of steps in the binomial tree
    div_yield (float): continuous dividend yield of the underlying asset
    div_dates (list): list of dividend payment dates (in years) relative to the present (e.g. [0.25, 0.5, 0.75])
    div_amounts (list): list of dividend amounts (in dollars) corresponding to the dividend payment dates

    Returns:
    float: price of the option
    """
    delta_t = T / N
    u = math.exp((r - div_yield) * delta_t + sigma * math.sqrt(delta_t))
    d = math.exp((r - div_yield) * delta_t - sigma * math.sqrt(delta_t))
    p = (math.exp((r - div_yield) * delta_t) - d) / (u - d)

    # Initialize stock prices at expiration
    stock_prices = [S * u**(N - i) * d**i for i in range(N + 1)]

    # Adjust stock prices for dividend payments
    for i in range(len(div_dates)):
        t = div_dates[i]
        div_amount = div_amounts[i]
        j = int(t / delta_t)
        stock_prices[j:] = [sp - div_amount for sp in stock_prices[j:]]

    # Initialize option values at expiration
    option_values = [max(0, K - stock_price) if option_type == 'call' else max(0, stock_price - K) for stock_price in stock_prices]

    # Calculate option values at each node in the tree
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            stock_price = S * u**(i - j) * d**j
            exercise_value = max(0, K - stock_price) if option_type == 'call' else max(0, stock_price - K)
            continuation_value = math.exp(-r * delta_t) * (p * option_values[j] + (1 - p) * option_values[j + 1])
            option_values[j] = max(exercise_value, continuation_value)

            # Adjust option values for dividend payments
            for k in range(len(div_dates)):
                t = div_dates[k]
                div_amount = div_amounts[k]
                if t > i * delta_t and t <= (i + 1) * delta_t:
                    option_values[j] += div_amount * math.exp(-r * (t - i * delta_t))

    return option_values[0]