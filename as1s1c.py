# ECE 9013 Assignment 1
# Section 1 Part C

import math

annual_salary = float(input("Enter your annual salary: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
down_payment = total_cost * 0.25
current_savings = 0
r = 0.04    # annual return
interest = annual_salary * r / 12
month = 0
a = 0
b = 1
iteration = 0
portion_saved = 0

def savings (portion_saved):
	global month
	global annual_salary
	global current_savings
	while month <= 35:
		monthly_salary = annual_salary / 12
		monthly_saved = monthly_salary * (portion_saved / 100)
		current_savings = current_savings + monthly_saved + (current_savings * r / 12)
		if month >= 6 and month % 6 == 0:
			annual_salary = annual_salary * (1 + semi_annual_raise)
		month = month + 1
	return current_savings
portion_saved = (a + b) / 2.0	
while abs(savings(portion_saved) - down_payment) < 100:
	if savings(portion_saved) < down_payment:
		a = portion_saved
	else:
		b = portion_saved
	iteration = iteration + 1
print(savings(portion_saved))
print(portion_saved)
print(month)
print("Rate: " + str(portion_saved / 100))
print("Steps in bisection search: " + str(iteration))