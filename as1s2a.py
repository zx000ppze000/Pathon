# ECE 9013 Assignment 1
# Section 2 Part A
# by Group 6: Tao Xu, Xu Zhang and Ziqi Yang

n = int(input("Please enter the number of Fibs: "))
a = 1   # 1st element of Fib
b = 1   # 2nd element of Fib
summ = a + b    # Sum of 1st and 2nd elements
i = 3   # Since the sum of first 2 elements has been
        # calculated, counter should start from 3

while i <= n:
    temp = a + b    # Temporary varible to store the
                    # sum of previous 2 elements
    a = b
    b = temp    # Update the value of new element by
                # the sum of previous two elements
    summ = summ + temp    # Do the summation
    i = i + 1   # Move to next element

print("The sum of Fibs is: ", summ)