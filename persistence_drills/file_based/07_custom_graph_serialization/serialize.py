"""Module: serialize.py
Author: Anurag"""

"""
Task 7: Custom Serialization for Complex Objects

Author: Anurag
Date: 2024-05-12
Description: Serialize a Graph object with complex data structures
"""

from graph import Graph

graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_edge("A", "B")

# Serialize
graph.save_to_file("graph.json")

print("✅ Graph serialized to graph.json")
