#!/usr/bin/env python3
"""
creator_scraped.py

Author: Anurag

Description:
Walks through the root directory, maps all folders and files,
and saves the structure to a JSON file for your delight.

Run it from the root folder you want to map:
$ python creator_scraped.py
"""

import os
import json

def map_directory(root_path):
    """
    Recursively maps folders and files under the given root directory.

    Args:
        root_path (str): The root directory path.

    Returns:
        dict: A nested dictionary mapping folder structure.
    """
    directory_map = {}

    for current_path, dirs, files in os.walk(root_path):
        rel_path = os.path.relpath(current_path, root_path)
        rel_path = '.' if rel_path == '.' else rel_path.replace("\\", "/")

        directory_map[rel_path] = {
            'folders': sorted(dirs),
            'files': sorted(files)
        }

    return directory_map

def save_map_as_json(directory_map, output_filename="folder_map.json"):
    """
    Saves the directory map to a JSON file.

    Args:
        directory_map (dict): The folder and file map.
        output_filename (str): Name of the JSON file to save.
    """
    with open(output_filename, 'w') as f:
        json.dump(directory_map, f, indent=4)
    print(f"📦 Folder map saved to {output_filename}")

if __name__ == "__main__":
    ROOT_DIR = os.getcwd()
    print(f"🔍 Scanning directory: {ROOT_DIR}")

    folder_map = map_directory(ROOT_DIR)
    save_map_as_json(folder_map)
