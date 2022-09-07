from data_structures.queue import Queue

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
        if start_node in self.adjacency_list:
            return self.adjacency_list[start_node]
        else:
            raise KeyError

    def get_nodes(self):
        return self.adjacency_list.keys()

    def size(self):
        return self.num

    def breadth_first(self, root):
        breadth = Queue()
        breadth.enqueue(root)
        visited = {root}
        node_list = []

        while not breadth.is_empty():
            curr_node = breadth.dequeue()
            node_list.append(curr_node.value)
            neighbors = self.get_neighbors(curr_node)
            for neighbor in neighbors:
                if neighbor.vertex not in visited:
                    visited.add(neighbor.vertex)
                    breadth.enqueue(neighbor.vertex)
        return node_list


class Vertex:

    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight
