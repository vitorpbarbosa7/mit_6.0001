import math

def calculate_months_to_down_payment(total_cost, portion_down_payment, annual_return_rate, annual_salary, portion_saved):
    # Convert the annual_return_rate to decimal form
    r = annual_return_rate / 12

    # Define the range for the search (0 to 10000)
    lower_bound = 0
    upper_bound = 10000

    # Use binary search to find the closest integer percentage within the range
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2  # Integer division
        current_savings = 0
        monthly_savings = (annual_salary / 12) * mid / 100  # Convert to decimal percentage
        for month in range(36):
            current_savings += monthly_savings + current_savings * r
        if abs(current_savings - (total_cost * portion_down_payment)) < 1:
            # If the difference is less than 1, we found a close percentage
            break
        elif current_savings < (total_cost * portion_down_payment):
            # If the savings are less, search the upper half
            lower_bound = mid + 1
        else:
            # If the savings are more, search the lower half
            upper_bound = mid - 1

    # Convert the found integer percentage to decimal form
    found_percentage = mid / 100

    return found_percentage

if __name__ == '__main__':
    starting_salary = 150000
    total_house_price = 1_000_000

    # Assume a portion_down_payment of 0.25 (25%)
    portion_down_payment = 0.25

    # Assume an annual_return_rate of 0.04 (4%)
    annual_return_rate = 0.04

    # Calculate the number of months required to reach the down payment
    found_percentage = calculate_months_to_down_payment(total_house_price, portion_down_payment, annual_return_rate, starting_salary, 1)

    print(f"Approximate savings percentage needed: {found_percentage:.2%}")
