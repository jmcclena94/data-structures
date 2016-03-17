# coding=utf-8


class SimpleGraph(object):
    """Create a simple graph"""

    def __init__(self):
        """Initialize a simple graph"""
        self.graph = {}

    def add_node(self, n):
        """Add a new node to the graph"""
        self.graph[n] = []

    def nodes(self):
        """Return a list of nodes"""
        return list(self.graph.keys())
