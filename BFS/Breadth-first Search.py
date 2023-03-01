import collections
import math


def BFS(parents, adj_list, queue, dists):
    while queue.__len__() != 0:
        u = queue.popleft()
        for neighbour in adj_list[u]:
            if dists[neighbour] == math.inf:
                dists[neighbour] = dists[u] + 1
                parents[neighbour] = u
                queue.append(neighbour)

def getPath(parents, start, end):
    path = []
    u = end
    while(u != start or parents[u] != u):
        path.append(u+1)
        u = parents[u]

    return path

if __name__ == '__main__':
    n, v1, v2 = list(map(int, input().split(' ')))

    adj_list = []

    for i in range(n):
        vertices = list(map(int, input().split(' ')))
        adj_line = []

        for id, vertex in enumerate(vertices):
            if vertex != 0:
                adj_line.append(id)

        adj_list.append(adj_line)

    dists = [math.inf] * n
    parents = [-1] * n
    parents[v1-1] = v1-1
    queue = collections.deque()
    queue.append(v1-1)
    dists[v1-1] = 0

    BFS(parents, adj_list, queue, dists)

    if dists[v2-1] == math.inf:
        print(-1)
    else:
        path = getPath(parents, v1-1, v2-1)

        print(dists[v2-1])
        path.append(v1)
        print(*path[::-1])

