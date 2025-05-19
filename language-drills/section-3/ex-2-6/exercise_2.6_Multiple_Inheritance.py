"""
Multiple Inheritance

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Combine Book with AudioMixin to create an AudioBook class using multiple inheritance.
"""

class AudioMixin:
    def play_audio(self):
        return f"Playing audio version of '{self.title}'"

class AudioBook(Book, AudioMixin):
    pass

audiobook = AudioBook("Sapiens", "Yuval Noah Harari")
print(audiobook)
print(audiobook.play_audio())
