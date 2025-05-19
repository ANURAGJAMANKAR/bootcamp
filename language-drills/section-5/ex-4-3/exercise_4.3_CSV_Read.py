"""
CSV Read

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import csv

# Assuming 'data.csv' exists with columns: 'name', 'age'
with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
