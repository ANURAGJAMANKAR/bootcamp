"""
Lazy CSV Filter

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import csv

def filter_csv(file_path, condition):
    """Generator to yield rows meeting a condition from a CSV."""
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if condition(row):
                yield row

# Example condition: Only yield rows where the first column is 'John'
file_path = 'data.csv'
for row in filter_csv(file_path, lambda row: row[0] == 'John'):
    print(row)
