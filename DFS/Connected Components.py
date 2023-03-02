
def DFS(u, global_visited, g, u_parent, visited_dots):
    visited_dots.append(u)
    global_visited[u] = True
    for neighbour in g[u]:
        if not global_visited[neighbour]:
            DFS(neighbour, global_visited, g, u, visited_dots)

import sys
import threading

sys.setrecursionlimit(10 ** 6)
threading.stack_size(10 ** 8)


def run():
    n, m  = list(map(int, input().split(' ')))

    g = [[] for y in range(n)]

    for i in range(m):
        a, b = list(map(int, input().split(' ')))
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    global_visited = [False] * n
    g_counts = [0] * n
    i = 0
    while i < n:
        if global_visited[i] == False:
            dots = []
            DFS(i, global_visited, g, -1, dots)
            g_counts[i] = len(dots)
            for dot in dots:
                g_counts[dot] = len(dots)
        i += 1

    print(*g_counts)


threading.Thread(target=run).start()