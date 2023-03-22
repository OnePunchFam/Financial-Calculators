# Stock intrinsic value calculator

def calculate_intrinsic_value(stock_price, earnings_per_share, growth_rate):
    intrinsic_value = earnings_per_share * (8.5 + (2 * growth_rate))
    margin_of_safety = intrinsic_value * 0.5
    return margin_of_safety / stock_price




# Example usage
stock_price = 100
earnings_per_share = 5
growth_rate = 0.1

intrinsic_value = calculate_intrinsic_value(stock_price, earnings_per_share, growth_rate)

print(f"Intrinsic value: {intrinsic_value:.2f}")