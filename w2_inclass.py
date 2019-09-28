# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 23:53:16 2018

@author: zhangx
"""
"""cube = int(input("please enter the no"))
epsilon = 0.001
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube :
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)"""
cube = int(input("please enter the no"))
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3- cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print ('num_guesses =', num_guesses)
print (guess, 'is close to the cube root of', cube)