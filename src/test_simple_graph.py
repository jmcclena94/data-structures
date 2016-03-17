# coding=utf-8
import pytest


def test_add_node():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_node('A')
    assert list(new_graph.graph.keys()) == ['A']
    assert new_graph.graph['A'] == []


def test_nodes():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A', 'B', 'C'], 'B': ['C', 'D']}
    assert new_graph.nodes() == ['A', 'B']
