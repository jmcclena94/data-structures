# coding=utf-8
import pytest


def test_add_node():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_node('A')
    assert list(new_graph.graph.keys()) == ['A']
    assert new_graph.graph['A'] == {}


def test_nodes():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'A', 10)
    new_graph.add_edge('A', 'B', 20)
    new_graph.add_edge('A', 'C', 30)
    new_graph.graph = {'A': ['A', 'B', 'C']}
    assert new_graph.nodes() == ['A']


def test_add_edge():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('B', 'A', 25)
    assert 'A' in new_graph.graph['B']
    assert new_graph.graph['B']['A'] == 25


def test_edges():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'B', 25)
    assert new_graph.edges() == [('A', 'B', 25)]


def test_del_node():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'B', 25)
    new_graph.add_edge('B', 'A', 10)
    new_graph.del_node('A')
    assert new_graph.graph == {'B': {}}


def test_del_node_error():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    with pytest.raises(KeyError):
        new_graph.del_node('A')


def test_del_edge():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'A', 10)
    new_graph.add_edge('A', 'B', 25)
    new_graph.del_edge('A', 'B')
    assert new_graph.graph == {'A': {'A': 10}, 'B': {}}


def test_del_edge_val_error():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'A', 10)
    new_graph.add_edge('A', 'B', 25)
    with pytest.raises(ValueError):
        new_graph.del_edge('A', 'E')


def test_del_edge_key_error():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'A', 10)
    new_graph.add_edge('A', 'B', 25)
    with pytest.raises(KeyError):
        new_graph.del_edge('G', 'C')


def test_has_node():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'A', 15)
    assert new_graph.has_node('A') is True
    assert new_graph.has_node('B') is False


def test_neighbors():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'B', 15)
    assert new_graph.neighbors('A') == ['B']


def test_neighbors_error():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'B', 15)
    with pytest.raises(KeyError):
        new_graph.neighbors('E')


def test_adjacent():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'A', 10)
    new_graph.add_edge('A', 'B', 25)
    new_graph.add_node('C')
    assert new_graph.adjacent('A', 'B') is True
    assert new_graph.adjacent('A', 'C') is False


def test_adjacent_error():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'A', 10)
    new_graph.add_edge('A', 'B', 25)
    with pytest.raises(KeyError):
        new_graph.adjacent('A', 'E')


def test_depth_first_traversal():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'B', 10)
    new_graph.add_edge('A', 'C', 20)
    new_graph.add_edge('B', 'D', 5)
    new_graph.add_edge('B', 'E', 3)
    new_graph.add_edge('E', 'F', 13)
    new_graph.add_edge('C', 'F', 16)
    visited = new_graph.dft('A')
    keys = list(new_graph.graph.keys())
    for val in visited:
        assert val in keys


def test_dft_cyclic():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'B', 10)
    new_graph.add_edge('A', 'C', 20)
    new_graph.add_edge('B', 'D', 5)
    new_graph.add_edge('B', 'E', 3)
    new_graph.add_edge('E', 'F', 13)
    new_graph.add_edge('C', 'F', 16)
    new_graph.add_edge('F', 'A', 100)
    visited = new_graph.dft('A')
    keys = list(new_graph.graph.keys())
    for val in visited:
        assert val in keys


def test_breadth_first_traversal():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'B', 10)
    new_graph.add_edge('A', 'C', 20)
    new_graph.add_edge('B', 'D', 5)
    new_graph.add_edge('B', 'E', 3)
    new_graph.add_edge('E', 'F', 13)
    new_graph.add_edge('C', 'F', 16)
    visited = new_graph.bft('A')
    keys = list(new_graph.graph.keys())
    for val in visited:
        assert val in keys


def test_bft_cyclic():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'B', 10)
    new_graph.add_edge('A', 'C', 20)
    new_graph.add_edge('B', 'D', 5)
    new_graph.add_edge('B', 'E', 3)
    new_graph.add_edge('E', 'F', 13)
    new_graph.add_edge('C', 'F', 16)
    new_graph.add_edge('F', 'A', 100)
    visited = new_graph.bft('A')
    keys = list(new_graph.graph.keys())
    for val in visited:
        assert val in keys


def test_bellman():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'B', 5)
    new_graph.add_edge('A', 'C', 20)
    new_graph.add_edge('B', 'D', 5)
    new_graph.add_edge('B', 'E', 3)
    new_graph.add_edge('E', 'F', 13)
    new_graph.add_edge('C', 'F', 16)
    new_graph.add_edge('F', 'A', 100)
    distance, path = new_graph.bellman('A', 'F')
    assert distance == 21
    assert path == ['A', 'B', 'E', 'F']


def test_dijkstra():
    from simple_graph import SimpleGraph
    new_graph = SimpleGraph()
    new_graph.add_edge('A', 'B', 5)
    new_graph.add_edge('A', 'C', 20)
    new_graph.add_edge('B', 'D', 5)
    new_graph.add_edge('B', 'E', 3)
    new_graph.add_edge('E', 'F', 13)
    new_graph.add_edge('C', 'F', 16)
    new_graph.add_edge('F', 'A', 100)
    distance, path = new_graph.dijkstra('A', 'F')
    assert distance == 21
    assert path == ['A', 'B', 'E', 'F']
