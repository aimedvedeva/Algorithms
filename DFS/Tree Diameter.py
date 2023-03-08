import sys
import threading

sys.setrecursionlimit(10 ** 6)
threading.stack_size(10 ** 8)

max_count = 0
max_vertex = 0


def DFS(u, adj_list, visited, count):
    global max_count, max_vertex
    visited[u] = True

    if count > max_count:
        max_count = count
        max_vertex = u

    for neighbour in adj_list[u]:
        if not visited[neighbour]:
            DFS(neighbour, adj_list, visited, count + 1)


def run():
    n = int(input())

    parents = []
    parents.append(1)
    parents = list(input().split(' '))

    adj_list = [[] for i in range(n)]

    for i in range(0, n - 1):
        a = i + 1
        b = int(parents[i]) - 1
        adj_list[b].append(a)
        adj_list[a].append(b)

    visited = [False] * n
    DFS(0, adj_list, visited, 0)

    visited = [False] * n
    DFS(max_vertex, adj_list, visited, 0)

    print(max_count)


threading.Thread(target=run).start()