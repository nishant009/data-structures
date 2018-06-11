import ast
import optparse
from collections import defaultdict
from graph import Graph

class DFS(object):
    _UNDISCOVERED = 0
    _DISCOVERED = 1
    _PROCESSED = 2

    def __init__(self):
        self._parent = defaultdict(int)
        self._entry = defaultdict(int)
        self._exit = defaultdict(int)
        self._state = defaultdict(int)
        self._time = 0

    def do_dfs(self, g, u):
        self._state[u] = self._DISCOVERED
        self._process_vertex(u)
        self._entry[u] = self._time
        self._time += 1

        for edge in g.get_edges(u):
            v = edge[g.KEY_END]
            self._process_edge(u, v)
            if self._state[v] == self._UNDISCOVERED:
                self._parent[v] = u
                self.do_dfs(g, v)
            
        self._state[u] = self._PROCESSED
        self._exit[u] = self._time
        self._time += 1

    def _process_vertex(self, v):
        return

    def _process_edge(self, u, v):
        print(u, '-->', v)


def main():
    """Example invocation:
    python dfs.py --vertices='[1, 2, 3, 4, 5, 6]' \
        --edges='[(1, 2), (1, 5), (1, 6), (2, 3), (2, 5), (3, 4), (4, 5)]' \
        --root=1
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

    options, _ = parser.parse_args()

    g = Graph()
    g.read_graph(
        ast.literal_eval(options.vertices),
        ast.literal_eval(options.edges)
    )

    print('Input graph:')
    g.print_graph()

    print('DFS traversal:')
    dfs = DFS()
    dfs.do_dfs(g, int(options.root))


if __name__ == "__main__":
    main()
