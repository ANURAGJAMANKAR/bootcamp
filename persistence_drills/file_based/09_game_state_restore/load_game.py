"""Module: state_manager.py
Author: Anurag"""

"""
Task 9: Restoring Object State (Game Session)

Author: Anurag
Date: 2024-05-12
Description: Save and restore the state of a game session
"""

from game import Game

# Create an empty game object
game = Game()

# Load state from file
game.load("game_state.json")

print("✅ Game state loaded:")
print(f"Level: {game.level}")
print(f"Score: {game.score}")
