import sys
import threading

sys.setrecursionlimit(10**6)
threading.stack_size(10**8)

T = 0

def DFS(u, adj_list, visited, t_in, t_out):
    global T
    visited[u] = True

    t_in[u] = T
    T+=1

    for neighbour in adj_list[u]:
        if not visited[neighbour]:
            DFS(neighbour, adj_list, visited, t_in, t_out)

    t_out[u] = T
    T+=1

def run():
    n = int(input())

    parents = list(map(int, input().split(' ')))

    adj_list = [[] for i in range(n)]
    adj_list[0] = [0]

    for i in range(0, n-1):
        a = i+1
        b = parents[i]-1
        adj_list[b].append(a)

    q = int(input())

    pairs = []
    for i in range(q):
        a, b = list(map(int, input().split(' ')))
        pairs.append((a-1,b-1))


    t_in = [0] * n
    t_out = [0] * n
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            DFS(i, adj_list, visited, t_in, t_out)

    for pair in pairs:
        a = pair[0]
        b = pair[1]
        if t_in[a] < t_in[b] and t_out[a] > t_out[b]:
            print(1)
        elif t_in[a] > t_in[b] and t_out[a] < t_out[b]:
            print(2)
        else:
            print(3)

threading.Thread(target=run).start()