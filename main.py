
# File: main.py
"""Main program that uses the math_utils module."""

# Method 1: Import entire module
import math_utils

result1 = math_utils.add(5, 3)
print(f"5 + 3 = {result1}")

result2 = math_utils.multiply(4, 7)
print(f"4 * 7 = {result2}")

print(f"PI = {math_utils.PI}")

# Method 2: Import specific functions
from math_utils import power, PI

result3 = power(2, 8)
print(f"2^8 = {result3}")

# Method 3: Import with alias
import math_utils as mu

result4 = mu.add(10, 20)
print(f"10 + 20 = {result4}")

# Method 4: Import all (not recommended for production)
# from math_utils import *
# result5 = add(1, 2)