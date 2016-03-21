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
    new_graph.graph = {'A': ['A', 'B', 'C']}
    assert new_graph.nodes() == ['A']


def test_add_edge():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A', 'B', 'C'], 'B': ['C', 'D']}
    new_graph.add_edge('B', 'A')
    assert 'A' in new_graph.graph['B']


def test_add_edge_no_nodes():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {}
    new_graph.add_edge('B', 'A')
    assert 'A' in new_graph.graph['B']


def test_edges():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A', 'B', 'C']}
    assert new_graph.edges() == [('A', 'A'), ('A', 'B'), ('A', 'C')]


def test_del_node():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A', 'B', 'C']}
    new_graph.del_node('A')
    assert new_graph.graph == {}


def test_del_node_edge():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A', 'B', 'C'], 'B': ['A', 'B']}
    new_graph.del_node('A')
    assert new_graph.graph == {'B': ['B']}


def test_del_node_error():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    with pytest.raises(KeyError):
        new_graph.del_node('A')


def test_del_edge():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A', 'B', 'C']}
    new_graph.del_edge('A', 'B')
    assert new_graph.graph == {'A': ['A', 'C']}


def test_del_edge_val_error():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A', 'B', 'C']}
    with pytest.raises(ValueError):
        new_graph.del_edge('A', 'E')


def test_del_edge_key_error():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A', 'B', 'C']}
    with pytest.raises(KeyError):
        new_graph.del_edge('G', 'C')


def test_has_node():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A']}
    assert new_graph.has_node('A') is True
    assert new_graph.has_node('B') is False


def test_neighbors():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A', 'B', 'C']}
    assert new_graph.neighbors('A') == ['A', 'B', 'C']


def test_neighbors_error():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A', 'B', 'C']}
    with pytest.raises(KeyError):
        new_graph.neighbors('E')


def test_adjacent():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A', 'B', 'C'], 'E': ['A'], 'B': []}
    assert new_graph.adjacent('A', 'B') is True
    assert new_graph.adjacent('A', 'E') is False


def test_adjacent_error():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['A', 'B', 'C']}
    with pytest.raises(KeyError):
        new_graph.adjacent('A', 'E')

def test_depth_first_traversal():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['B', 'C'],
                       'B': ['D', 'E'],
                       'D': [],
                       'E': ['F'],
                       'C': ['F'],
                       'F': [],
                       }
    assert new_graph.dft("A") == ['A', 'C', 'F', 'B', 'E', 'D']

def test_dft_cyclic():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['B', 'C'],
                       'B': ['D', 'E'],
                       'D': [],
                       'E': ['F'],
                       'C': ['F'],
                       'F': ['A'],
                       }
    assert new_graph.dft("A") == ['A', 'C', 'F', 'B', 'E', 'D']

def test_breadth_first_traversal():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['B', 'C'],
                       'B': ['D', 'E'],
                       'D': [],
                       'E': ['F'],
                       'C': ['F'],
                       'F': [],
                       }
    assert new_graph.bft("A") == ['A', 'C', 'B', 'F', 'E', 'D']

def test_bft_cyclic():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['B', 'C'],
                       'B': ['D', 'E'],
                       'D': [],
                       'E': ['F'],
                       'C': ['F'],
                       'F': ['A'],
                       }
    assert new_graph.bft("A") == ['A', 'C', 'B', 'F', 'E', 'D']
