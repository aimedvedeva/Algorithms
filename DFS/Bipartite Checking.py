import sys
import threading

sys.setrecursionlimit(10**6)
threading.stack_size(10**8)

is_bipartite = True

def DFS(u, colors_visited, adj_list, color):
    global is_bipartite
    colors_visited[u] = color
    for neighbour in adj_list[u]:
        if colors_visited[neighbour] == colors_visited[u]:
            is_bipartite = False
        if colors_visited[neighbour] == -1:
            DFS(neighbour, colors_visited, adj_list, (color + 1) % 2)

def run():
    n, m  = list(map(int, input().split(' ')))

    adj_list = [[] for y in range(n)]

    for i in range(m):
        a, b = list(map(int, input().split(' ')))
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)

    colors_visited = [-1] * n

    color = 0
    for i in range(n):
        if colors_visited[i] == -1:
            DFS(i, colors_visited, adj_list, color)

    print("YES") if is_bipartite else print("NO")


threading.Thread(target=run).start()