#! /usr/local/bin/python
from graph import Graph


def do_dfs(g):
    print('woof')


def main():
    g = Graph()
    g.read_graph(
        [1, 2, 3, 4, 5, 6],
        [(1, 2), (1, 5), (1, 6), (2, 3), (2, 5), (3, 4), (4, 5)]
    )

    g.print_graph()
    do_dfs(g)


if __name__ == "__main__":
    main()
