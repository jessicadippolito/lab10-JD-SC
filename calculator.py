"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a + b
def subtract(a,b):
    return a-b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return a/b
def logarithm(a, b):
    try:
        return math.log(b, a)
    except:
        raise ValueError


def exp(a, b):
    return a ** b
    return a + b

