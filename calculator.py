import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return b/a
    except:
        raise ZeroDivisionError

def logarithm(a,b):
    try:
        return math.log(b,a)
    except:
        raise ValueError

def exponent(a,b):
    return a**b



