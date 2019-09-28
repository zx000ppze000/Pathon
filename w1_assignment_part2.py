# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 05:17:44 2018

@author: zhangx
"""

total_cost = int(input("How much does your dream house cost?"))
portion_down_payment = total_cost*0.25
print(portion_down_payment)
current_savings = 0
month = 0
first_sixmonth = 0
return_rate = 0.04
annual_salary = int(input("What is your annual salary?"))
portion_saved = float(input("What is your portion saved?"))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))
monthly_saved = annual_salary /12 * portion_saved
print(monthly_saved)
while (first_sixmonth < 6):
    current_savings = current_savings + current_savings * return_rate / 12 + monthly_saved
    first_sixmonth += 1
    monthly_saved_raise = monthly_saved
if (current_savings < portion_down_payment):
    monthly_saved_raise = monthly_saved_raise * (1+semi_annual_raise)
    for i in range (0,6):
        i += 1
        current_savings = current_savings + current_savings * return_rate / 12 + monthly_saved_raise
    month += 6
else:
    f_month = month + 6
    print("Number of months are: ", f_month)