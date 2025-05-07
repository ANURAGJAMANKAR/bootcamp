"""
Write Small Functions

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

def get_scores():
    return [88, 92, 75]

def compute_average(scores):
    return sum(scores) / len(scores)

def display_average(avg):
    print(f"Average score: {avg:.2f}")

# Usage
scores = get_scores()
avg = compute_average(scores)
display_average(avg)
