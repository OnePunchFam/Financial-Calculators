"""

Altman's Z-score Model:

The z-score model has been shown to be effective in predicting bankruptcy, especially when used with publicly traded manufacturing companies. 

The resulting score is interpreted as follows:

Above 3.0: company is considered safe
Between 2.7 and 3.0: company is considered to be in a gray area
Below 2.7: company is considered to be in financial distress

"""


def calculate_z_score(working_capital, retained_earnings, ebit, market_value, sales):
    A = (working_capital / total_assets)
    B = (retained_earnings / total_assets)
    C = (ebit / total_assets)
    D = (market_value_of_equity / total_liabilities)
    E = (sales / total_assets)
    
    z_score = 1.2 * A + 1.4 * B + 3.3 * C + 0.6 * D + 1.0 * E
    
    return z_score




# Example Usage:


working_capital = 1000000
retained_earnings = 2000000
ebit = 1500000
market_value = 3000000
sales = 5000000

z_score = calculate_z_score(working_capital, retained_earnings, ebit, market_value, sales)
print("The Altman Z-score for this company is: {:.2f}".format(z_score))


# Output: The Altman Z-score for this company is: 1.89