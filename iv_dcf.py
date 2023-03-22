import numpy as np

def calculate_intrinsic_value(free_cash_flows, discount_rate, terminal_growth_rate):
    terminal_value = free_cash_flows[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
    present_values = [cf / (1 + discount_rate)**i for i, cf in enumerate(free_cash_flows)]
    present_values.append(terminal_value / (1 + discount_rate)**(len(free_cash_flows)))
    present_value_sum = np.sum(present_values)
    return present_value_sum



# Example Usage:

free_cash_flows = [100, 200, 300, 400, 500]
discount_rate = 0.1
terminal_growth_rate = 0.02

intrinsic_value = calculate_intrinsic_value(free_cash_flows, discount_rate, terminal_growth_rate)
print("The intrinsic value of the company is: {:.2f}".format(intrinsic_value))