# ECE 9013 Assignment 1
# Section 2 Part B
# by Group 6: Tao Xu, Xu Zhang and Ziqi Yang

n=int(input("Enter n: "))  # input interger n
a = 1                    # n start from 1
for i in range(1,n+1):   # Loop while in range(1,n+1)
    a = a * i            # Calculate factorial
print("n! = ", a)                 # output n!

r=int(input("Enter r: "))  # input interger r
b = 1                    # r start from 1
for o in range(1,r+1):   # Loop while in range(1,r+1)
    b = b * o            # Calculate factorial
print("r! = ", b)                 # output r!

x=n-r                    # identify x=n-r
for p in range(1,x):     # Loop while in range(1,x)
    x = x * p            # Calculate factorial

print("Final ouput: ",a/b/x)  # output final result (n/r)