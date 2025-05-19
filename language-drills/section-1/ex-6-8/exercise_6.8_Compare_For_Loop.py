"""
Compare For Loop

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Compares list comprehension vs generator expression
for filtering even numbers.
"""

list_comp = [x for x in range(10) if x % 2 == 0]
gen_expr = (x for x in range(10) if x % 2 == 0)

print("List:", list_comp)
print("Generator:", list(gen_expr))  # Convert to list to view

# Bonus: Memory footprint comparison
import sys
print("List comprehension size:", sys.getsizeof(list_comp))
print("Generator expression size:", sys.getsizeof(gen_expr))
