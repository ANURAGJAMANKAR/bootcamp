"""
Override Method

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Override the describe method in Novel to add a "Novel:" prefix.
"""

class Novel(Book):
    def describe(self):
        return f"Novel: '{self.title}' by {self.author}"
