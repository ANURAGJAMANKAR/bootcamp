

import json
import os
from typing import Dict, Any, List
from datetime import datetime

class GameSession:
    """
    A class representing a game session with save and load capabilities.

    Attributes:
        player_name (str): Name of the player
        level (int): Current game level
        score (int): Player's current score
        inventory (List[str]): Player's current inventory items
    """

    def __init__(
        self, 
        player_name: str, 
        level: int = 1, 
        score: int = 0, 
        inventory: List[str] = None
    ):
        """
        Initialize a GameSession object.

        Args:
            player_name (str): Name of the player
            level (int, optional): Starting game level. Defaults to 1.
            score (int, optional): Starting score. Defaults to 0.
            inventory (List[str], optional): Starting inventory. Defaults to None.
        """
        self.player_name = player_name
        self.level = level
        self.score = score
        self.inventory = inventory or []
        self.created_at = datetime.now().isoformat()

    def progress_level(self) -> None:
        """
        Advance the player to the next level.
        """
        self.level += 1
        self.score += 100  # Bonus points for leveling up

    def collect_item(self, item: str) -> None:
        """
        Add an item to the player's inventory.

        Args:
            item (str): Item to be added to inventory
        """
        if item not in self.inventory:
            self.inventory.append(item)
            self.score += 50  # Bonus points for collecting item

    def save_game(self, save_path: str) -> None:
        """
        Save the current game state to a JSON file.

        Args:
            save_path (str): Path to save the game state
        """
        # Ensure the directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Prepare game state data
        game_state = {
            "player_name": self.player_name,
            "level": self.level,
            "score": self.score,
            "inventory": self.inventory,
            "created_at": self.created_at,
            "saved_at": datetime.now().isoformat()
        }

        try:
            with open(save_path, 'w') as file:
                json.dump(game_state, file, indent=2)
            print(f"Game state saved to {save_path}")
        except IOError as e:
            print(f"Error saving game state: {e}")
            raise

    @classmethod
    def load_game(cls, save_path: str) -> 'GameSession':
        """
        Load a previously saved game state from a JSON file.

        Args:
            save_path (str): Path to the saved game state file

        Returns:
            GameSession: Restored game session
        """
        try:
            with open(save_path, 'r') as file:
                game_state = json.load(file)

            # Recreate the game session
            game_session = cls(
                player_name=game_state['player_name'],
                level=game_state['level'],
                score=game_state['score'],
                inventory=game_state['inventory']
            )

            # Restore original creation timestamp
            game_session.created_at = game_state['created_at']

            print(f"Game state loaded from {save_path}")
            return game_session
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading game state: {e}")
            raise

def main():
    """
    Demonstrate game state saving and loading.
    """
    # Create initial game session
    game = GameSession("Anurag")
    
    # Simulate some game progress
    print("Initial Game State:")
    print(f"Player: {game.player_name}")
    print(f"Level: {game.level}")
    print(f"Score: {game.score}")
    print(f"Inventory: {game.inventory}")

    # Progress through the game
    game.progress_level()
    game.collect_item("Magic Sword")
    game.collect_item("Health Potion")

    # Save game state
    save_path = "data/serialized/task9/game_save.json"
    game.save_game(save_path)

    # Simulate game interruption
    print("\nGame progressed and saved...")

    # Load saved game state
    try:
        loaded_game = GameSession.load_game(save_path)

        # Print loaded game state
        print("\nLoaded Game State:")
        print(f"Player: {loaded_game.player_name}")
        print(f"Level: {loaded_game.level}")
        print(f"Score: {loaded_game.score}")
        print(f"Inventory: {loaded_game.inventory}")
        print(f"Created At: {loaded_game.created_at}")

    except Exception as e:
        print(f"Failed to load game state: {e}")

if __name__ == "__main__":
    main()