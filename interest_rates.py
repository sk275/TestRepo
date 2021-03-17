def int_rate(r, n, t):

    """
    Returns the interest earned over t years.
    N: compounding frequency
    r: net interest rate 
    """

    return (1+r/n)**(n*t)

def add_method(a, b):
    return a+b

def subtract_method(a, b):
    return a-b

def divide_method(x,y):
    return x/y
