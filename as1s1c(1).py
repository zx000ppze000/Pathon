# ECE 9013 Assignment 1
# Section 1 Part C
# by Group 6: Tao Xu, Xu Zhang and Ziqi Yang

annual_salary = float(input("Enter your annual salary: "))
k = annual_salary	# Extra varible to store original annual salary because 
					# annual_salary will be modified during iteration
total_cost = 1000000.0		# Cost of the house is $1M
semi_annual_raise = 0.07	# Semi-annual raise is 7%
down_payment = total_cost * 0.25    # Get the amount of down payment (25% of total)
current_savings = 0		# Initialize current savings
r = 0.04    # Annual rate
month = 0	# Initialize number of months
iteration = 0	# Bisection steps
portion_saved = 0	# Initialize saving portion

a = 0	# Low guess value, in percentage
b = 100.0	# High guess value, in percentage
portion_saved = (a + b) / 2.0	# First bisection guess, in percentage
while month <= 36:	# Calculating the saving amount after 36 months when
					# portion_saved = 100% to check if the annual salary
					# is possible to pay the down payment
	monthly_salary = annual_salary / 12    # Use annual salary to get monthly salary
	monthly_saved = monthly_salary * (100.0 / 100.0)	# The amount need to be saved when
														# portion_saved = 100%
	current_savings = current_savings + monthly_saved + (current_savings * r / 12)
					# Update new saving amount by adding monthly saving amount and interest			
	if month >= 6 and month % 6 == 0:	# Increase salary by every 6 months (after 6 months)
		annual_salary = annual_salary * (1 + semi_annual_raise)
	month = month + 1	# Increase month number by 1
if down_payment > current_savings:	# Check if it is possible to pay the down payment
	print("It is not possible to pay the down payment in three years.")
	exit(1)		# Exit this program if it is impossible to pay the down payment
while abs(current_savings - down_payment) > 100:	# When the saving amount is within $100,
													# then finishing bisection search
	annual_salary = k	# Reset the annual salary to original value after each iteration
	current_savings = 0	# Reset saving amount after each iteration
	month = 0	# Reset number of months after each iteration
	while month <= 36:	# To calculate the saving amount after 36 months
		monthly_salary = annual_salary / 12		# Use annual salary to get monthly salary
		monthly_saved = monthly_salary * (portion_saved / 100.00)	
						# The amount need to be saved in specific portion_saved
		current_savings = current_savings + monthly_saved + (current_savings * r / 12)
						# Update new saving amount by adding monthly saving amount and interest
		if month >= 6 and month % 6 == 0:	# Increase salary by every 6 months (after 6 months)
			annual_salary = annual_salary * (1 + semi_annual_raise)
		month = month + 1	# Count the month number
	if current_savings < down_payment:
		a = portion_saved	# If the guess is low, start a new guess in right halfway
	else:
		b = portion_saved	# If the guess is high, start a new guess in left halfway
	portion_saved = (a + b) / 2.0	# Move to next guess
	iteration = iteration + 1	# Increase month number by 1

# Output the saving portion rate and steps in bisection search
print("Rate: " + str(portion_saved / 100))
print("Steps in bisection search: " + str(iteration))