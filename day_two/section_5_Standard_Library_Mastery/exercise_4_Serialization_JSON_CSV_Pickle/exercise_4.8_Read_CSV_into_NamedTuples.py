"""
Read CSV into NamedTuples

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import csv
from collections import namedtuple

# Define a namedtuple type for CSV rows
Row = namedtuple('Row', ['name', 'age'])

# Read CSV into namedtuples
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        row_named = Row(*row)  # Convert each row to a namedtuple
        print(row_named)
