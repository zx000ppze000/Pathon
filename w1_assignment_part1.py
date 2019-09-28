# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 04:19:09 2018

@author: zhangx
"""

total_cost = int(input("How much does your dream house cost?"))
portion_down_payment = total_cost*0.25
print(portion_down_payment)
current_savings = 0
month = 0
return_rate = 0.04
annual_salary = int(input("What is your annual salary?"))
portion_saved = float(input("What is your portion saved?"))
monthly_saved = annual_salary/12 * portion_saved
print(monthly_saved)
while (current_savings < portion_down_payment):
    current_savings = current_savings + current_savings * return_rate / 12 + monthly_saved
    month += 1
    if (current_savings > portion_down_payment):
        print("Number of months are: ", month)