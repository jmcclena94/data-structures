# coding=utf-8


class SimpleGraph(object):
    """Create a simple graph."""

    def __init__(self):
        """Initialize a simple graph."""
        self.graph = {}

    def add_node(self, n):
        """Add a new node to the graph."""
        self.graph[n] = {}

    def nodes(self):
        """Return a list of nodes."""
        return list(self.graph.keys())

    def add_edge(self, n1, n2, weight):
        """Add an edge to the graph pointing from n1 to n2."""
        node_list = list(self.graph.keys())
        if n1 not in node_list:
            self.add_node(n1)
        if n2 not in node_list:
            self.add_node(n2)
        self.graph[n1][n2] = weight

    def edges(self):
        """Return a list of all edges in the graph."""
        node_list = list(self.graph.keys())
        edge_list = []
        for node in node_list:
            edges = list(self.graph[node].keys())
            for edge in edges:
                edge_val = (node, edge, self.graph[node][edge])
                edge_list.append(edge_val)
        return edge_list

    def del_node(self, n):
        """Delete a node from the graph."""
        try:
            self.graph.pop(n)
            node_list = list(self.graph.keys())
            for node in node_list:
                if n in self.graph[node]:
                    self.graph[node].pop(n)
        except KeyError:
            raise KeyError

    def del_edge(self, n1, n2):
        """Delete the edge from n1 to n2."""
        try:
            if n2 in self.graph[n1]:
                self.graph[n1].pop(n2)
            else:
                raise ValueError
        except KeyError:
            raise KeyError

    def has_node(self, n):
        """Check if the graph has node n."""
        node_list = list(self.graph.keys())
        return n in node_list

    def neighbors(self, n):
        """Return the neighbors of node n."""
        try:
            return list(self.graph[n].keys())
        except KeyError:
            raise KeyError

    def adjacent(self, n1, n2):
        """Check if n1 is connected to n2"""
        try:
            self.graph[n2]
            return n2 in self.graph[n1]
        except KeyError:
            raise KeyError

    def dft(self, start):
        """Return a list of visited nodes for depth first traversal."""
        to_visit = [start]
        visited = []
        while to_visit:
            next_val = to_visit.pop()
            if next_val not in visited:
                visited.append(next_val)
                to_visit = to_visit + list(self.graph[next_val].keys())
        return visited

    def bft(self, start):
        """Return a list of visited nodes for breadth first traversal."""
        to_visit = [start]
        visited = []
        while to_visit:
            next_val = to_visit.pop()
            if next_val not in visited:
                visited.append(next_val)
                to_visit = list(self.graph[next_val].keys()) + to_visit
        return visited

    def bellman(self, node1, node2):
        """Return the shortest visit path of a graph."""
        distance_dict = {}
        for key in self.graph:
            if key == node1:
                distance_dict[key] = {'distance': 0, 'path': [node1]}
            else:
                distance_dict[key] = {'distance': float('inf'), 'path': []}
        visited = []
        to_visit = [node1]
        while to_visit:
            parent = to_visit.pop()
            if parent not in visited:
                children = list(self.graph[parent].keys())
                for child in children:
                    n1_distance = distance_dict[child]['distance']
                    weighted_distance = distance_dict[
                        parent]['distance'] + self.graph[parent][child]
                    # import pdb;pdb.set_trace()
                    if n1_distance > weighted_distance:
                        distance_dict[child]['distance'] = weighted_distance
                        distance_dict[child]['path'] = distance_dict[
                            parent]['path'] + [child]
                to_visit = children + to_visit
            visited.append(parent)
        return distance_dict[node2]['distance'], distance_dict[node2]['path']

    def dijkstra(self, node1, node2):
        """Return the shortest visit path of a graph."""
        distance_dict = {}
        for key in self.graph:
            if key == node1:
                distance_dict[key] = {'distance': 0, 'path': [node1]}
            else:
                distance_dict[key] = {'distance': float('inf'), 'path': []}
        visited = []
        to_visit = [node1]
        while to_visit:
            parent = to_visit.pop()
            print(parent)
            if parent not in visited:
                children_dict = self.graph[parent]
                children_wgt = []
                for key, val in children_dict.items():
                    children_wgt.append([key, val])
                children_sort = sorted(
                                children_wgt, key=lambda child: child[1])
                for child in children_sort:
                    n1_distance = distance_dict[child[0]]['distance']
                    weighted_distance = distance_dict[
                        parent]['distance'] + child[1]
                    if n1_distance > weighted_distance:
                        distance_dict[child[0]]['distance'] = weighted_distance
                        distance_dict[child[0]]['path'] = distance_dict[
                            parent]['path'] + [child[0]]
                to_visit = list(self.graph[parent].keys()) + to_visit
            visited.append(parent)
        return distance_dict[node2]['distance'], distance_dict[node2]['path']

if __name__ == '__main__':
    new_graph = SimpleGraph()
    new_graph.graph = {'A': {'B': 10, 'C': 20},
                       'B': {'D': 5, 'E': 3},
                       'D': {},
                       'E': {'F': 13},
                       'C': {'F': 16},
                       'F': {'A': 100},
                       }
    dft = new_graph.dft('A')
    bft = new_graph.bft('A')
    print("Depth first traversal:" + str(dft))
    print("Breadth first traversal:" + str(bft))
    new_graph.add_edge('F', 'C', 10)
    dft = new_graph.dft('A')
    bft = new_graph.bft('A')
    print("Depth first traversal(cyclic):" + str(dft))
    print("Breadth first traversal(cyclic):" + str(bft))
