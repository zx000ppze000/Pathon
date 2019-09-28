# ECE 9013 Assignment 1
# Section 2 Part C
# by Group 6: Tao Xu, Xu Zhang and Ziqi Yang

n=int(input("Enter n: "))  # manual input n,x,a
x=int(input("Enter x: "))
a=int(input("Enter a: "))

def getFact(n): # Identify function named getFact(Calculate factorial)
    result=1    # when i=1 the result of factorial is 1
    for i in range(2,n+1):  # loop when i in range(2,n+1)
        result*=i           # result=result*i(3!=3*2!)
    return result           # Loop return 

bin=0                   # bin starts from zero
for k in range(0,n+1):  # Loop if K in range of (0,n+1)
   part1=getFact(n)/getFact(k)/getFact(n-k)  # formula of (n/k)
   part2=x**k           # x^k
   part3=a**(n-k)       # a^(n-k)
   step_bin=part1*part2*part3  # result of each step
   bin+=step_bin        # get sum using +=
   
print("Final result of bin: ", bin)              # output final result bin