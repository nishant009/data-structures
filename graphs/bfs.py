import ast
import optparse
from collections import defaultdict, deque
from graph import Graph

class BFS(object):
    _UNDISCOVERED = 0
    _DISCOVERED = 1
    _PROCESSED = 2

    def __init__(self):
        self._parent = defaultdict(int)
        self._level = {}

    def do_bfs(self, g, s):
        state = defaultdict(int)
        queue = deque()

        state[s] = self._DISCOVERED
        self._level[s] = 0
        queue.append(s)

        curr_level = 0
        while len(queue) > 0:
            u = queue.popleft()
            self._process_vertex_early(u)
            state[u] = self._PROCESSED

            if curr_level != self._level[u]:
                curr_level += 1

            for edge in g.get_edges(u):
                v = edge[g.KEY_END]

                # Ensure an edge is processed only once
                if state[v] != self._PROCESSED or g.is_directed():
                    self._process_edge(u, v)

                if state[v] == self._UNDISCOVERED:
                    queue.append(v)
                    state[v] = self._DISCOVERED
                    self._parent[v] = u
                    self._level[v] = curr_level + 1
            self._process_vertex_late(u)

    def _process_vertex_early(self, v):
        return


    def _process_vertex_late(self, v):
        return

    def _process_edge(self, u, v):
        print(u, '-->', v)

    def find_path(self, v):
        """Find the shortest path from root to input vertex v"""
        if self._parent[v] == 0:
            print(v)
        else:
            self.find_path(self._parent[v])
            print(v)

    def get_parents(self):
        return self._parent

    def get_levels(self):
        return self._level

def main():
    """Example invocation:
    python bfs.py --vertices='[1, 2, 3, 4, 5, 6]' \
        --edges='[(1, 2), (1, 5), (1, 6), (2, 3), (2, 5), (3, 4), (4, 5)]' \
        --root=1 --destination=4
    """
    parser = optparse.OptionParser()
    parser.add_option(
        '-v',
        '--vertices',
        action='store',
        dest='vertices',
        help='List of vertices',
        default=[]
    )
    parser.add_option(
        '-e',
        '--edges',
        action='store',
        dest='edges',
        help='List of tuples (x, y) representing an edge between vertices x and y',
        default=[]
    )
    parser.add_option(
        '-r',
        '--root',
        action='store',
        dest='root',
        help='Root node of the graph',
        default=1
    )

    parser.add_option(
        '-d',
        '--destination',
        action='store',
        dest='destination',
        help='Destination node in the graph for shortest path',
        default=2
    )

    options, _ = parser.parse_args()

    g = Graph()
    g.read_graph(
        ast.literal_eval(options.vertices),
        ast.literal_eval(options.edges)
    )

    print('Input graph:')
    g.print_graph()

    print('BFS traversal:')
    bfs = BFS()
    bfs.do_bfs(g, int(options.root))

    print('Shortest path for ', options.destination, ':')
    bfs.find_path(int(options.destination))

    print('Levels: ')
    levels = bfs.get_levels()
    for key in levels:
        print(key, ': ', levels[key])

if __name__ == '__main__':
    main()
