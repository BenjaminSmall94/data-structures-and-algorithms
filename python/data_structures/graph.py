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

    def get_node(self, name):
        for vertex in self.adjacency_list.keys():
            if vertex.value == name:
                return vertex
        raise KeyError

    def get_nodes(self):
        return self.adjacency_list.keys()

    def size(self):
        return self.num

    def contains(self, name):
        return name in [vertex.value for vertex in self.adjacency_list.keys()]

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

    def depth_first_search(self, root):
        def search_node(curr_node):
            node_list.append(curr_node.value)
            visited_nodes.add(curr_node)
            for neighbor_edge in self.get_neighbors(curr_node):
                if neighbor_edge.vertex not in visited_nodes:
                    search_node(neighbor_edge.vertex)
            return node_list

        if root not in self.adjacency_list:
            return []
        node_list = []
        visited_nodes = set()
        return search_node(root)


class Vertex:

    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight
