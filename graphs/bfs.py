#! /usr/local/bin/python

import ast
import optparse
from collections import defaultdict, deque
from graph import Graph

UNDISCOVERED = 0
DISCOVERED = 1
PROCESSED = 2


def do_bfs(g, s):
    state = defaultdict(int)
    parent = defaultdict()
    queue = deque()

    state[s] = DISCOVERED
    queue.append(s)

    while len(queue) > 0:
        u = queue.popleft()
        process_vertex_early(u)
        state[u] = PROCESSED

        for edge in g.get_edges(u):
            v = edge[g.KEY_END]

            # Ensure an edge is processed only once
            if state[v] != PROCESSED or g.is_directed():
                process_edge(u, v)

            if state[v] == UNDISCOVERED:
                queue.append(v)
                state[v] = DISCOVERED
                parent[v] = u
        process_vertex_late(u)

    print(str(parent))


def process_vertex_early(v):
    return


def process_vertex_late(v):
    return

def process_edge(u, v):
    print(u, "-->", v)


def main():
    """Example invocation:
    ./bfs.py --vertices="[1, 2, 3, 4, 5, 6]" \
        --edges="[(1, 2), (1, 5), (1, 6), (2, 3), (2, 5), (3, 4), (4, 5)]" \
        --root=1
    """
    parser = optparse.OptionParser()
    parser.add_option(
        '-v',
        '--vertices',
        action="store",
        dest="vertices",
        help="List of vertices",
        default=[]
    )
    parser.add_option(
        '-e',
        '--edges',
        action="store",
        dest="edges",
        help="List of tuples (x, y) representing an edge between vertices x and y",
        default=[]
    )
    parser.add_option(
        '-r',
        '--root',
        action="store",
        dest="root",
        help="Root node of the graph",
        default=[]
    )

    options, _ = parser.parse_args()

    g = Graph()
    g.read_graph(
        ast.literal_eval(options.vertices),
        ast.literal_eval(options.edges)
    )

    print('Input graph:')
    g.print_graph()

    print("BFS traversal:")
    do_bfs(g, int(options.root))


if __name__ == "__main__":
    main()
