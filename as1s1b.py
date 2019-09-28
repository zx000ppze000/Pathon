# ECE 9013 Assignment 1
# Section 1 Part B
# by Group 6: Tao Xu, Xu Zhang and Ziqi Yang

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
down_payment = total_cost * 0.25    # Get the amount of down payment (25% of total)
current_savings = 0     # Initialize current savings
r = 0.04    # Annual rate
month = 0   # Initialize number of months

while current_savings < down_payment:
    monthly_salary = annual_salary / 12     # Use annual salary to get monthly salary
    monthly_saved = monthly_salary * portion_saved  # The saving amount of each month in
                                                    # specific saving portion
    current_savings = current_savings + monthly_saved + (current_savings * r / 12)
                    # Update new saving amount by adding monthly saving amount and interest
    if month >= 6 and month % 6 == 0:   # Increase salary by every 6 months (after 6 months)
        annual_salary = annual_salary * (1 + semi_annual_raise)
    month = month + 1   # Count the month number

print("Number of months: " + str(month))