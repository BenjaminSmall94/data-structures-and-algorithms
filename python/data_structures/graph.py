class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.num = 0
        self.adjacency_list = {}

    def add_node(self, value):
        self.num += 1
        new_vertex = Vertex(value)
        self.adjacency_list[new_vertex] = []
        return new_vertex

    def add_edge(self, start_node, end_node, weight=None):
        if start_node in self.adjacency_list and end_node in self.adjacency_list:
            self.adjacency_list[start_node].append(Edge(end_node, weight))
        else:
            raise KeyError

    def get_neighbors(self, start_node):
        return self.adjacency_list[start_node]

    def get_nodes(self):
        return self.adjacency_list.keys()

    def size(self):
        return self.num


class Vertex:

    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight
