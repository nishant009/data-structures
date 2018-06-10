from collections import defaultdict


class Graph(object):
    KEY_END = 'end'
    KEY_WEIGHT = 'weight'

    def __init__(self, directed=False):
        self._vertices = []
        self._edges = defaultdict(list)
        self._num_edges = 0
        self._directed = directed

    def read_graph(self, vertices, edges):
        """Reads in a graph in terms of its edges.
        vertices -- a list of vertices.
        edges -- a list of tuples where
            each tuple (x, y) represents
            an edge between x and y.
            x and y should be vertices
        """
        for vertex in vertices:
            self._vertices.append(vertex)

        for x, y in edges:
            if x in self._vertices and y in self._vertices:
                self._insert_edge(x, y)
            else:
                self._vertices.clear()
                self._edges.clear()
                print('Bad edge specified. One of the nodes ', x, ' or ',
                      y, ' does not exist in the list of vertices')

    def _insert_edge(self, x, y, reverse_edge=False):
        self._edges[x].append(
            {
                self.KEY_END: y,
                self.KEY_WEIGHT: None,
            }
        )
        self._num_edges += 1

        if self._directed == False and reverse_edge == False:
            self._insert_edge(y, x, True)

    def get_num_vertices(self):
        return len(self._vertices)

    def get_num_edges(self):
        return self._num_edges

    def get_edges(self, x):
        if x in self._vertices:
            return self._edges[x]
        else:
            return []

    def is_directed(self):
        return self._directed

    def get_degree(self, x):
        if x in self._vertices:
            return len(self._edges[x])
        else:
            print('Unknown node')

    def print_graph(self):
        for vertex in self._vertices:
            for edge in self._edges[vertex]:
                print('Start: ', vertex, ', End: ',
                      edge[self.KEY_END], ', Weight: ', edge[self.KEY_WEIGHT])
