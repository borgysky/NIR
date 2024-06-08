import math

def calculate_function(x):
    if x < 0:
        raise ValueError("x должен быть неотрицательным")
    y = x**2 * math.sin(4 * math.sqrt(x))
    return y
