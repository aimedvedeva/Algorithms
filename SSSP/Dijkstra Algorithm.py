import math

if __name__ == '__main__':
    n, m, v1, v2 = list(map(int, input().split(' ')))

    arcs = []

    for i in range(m):
        a, b, w = list(map(int, input().split(' ')))
        arcs.append([a-1, b-1, w])
        arcs.append([b-1, a-1, w])

    d = [math.inf] * n
    d[v1-1] = 0

    parents = [-1] * n
    parents[v1-1] = v1-1

    visited = [False] * n


    while True:
        # find unvisited vertex with minimal d[u]
        u = -1
        min_d = math.inf
        for id, flag in enumerate(visited):
            if flag == False:
                if d[id] < min_d:
                    min_u = d[id]
                    u = id

        if u == -1 or d[u] == math.inf:
            break

        visited[u] = True

        for arc in arcs:
            u = arc[0]
            v = arc[1]
            w = arc[2]
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                parents[v] = u


    answer = -1 if d[v2-1] == math.inf else d[v2-1]
    print(answer)



