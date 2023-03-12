def find(u, p):
    if p[u] != u:
        p[u] = find(p[u], p)
    return p[u]

def union(u, v, p, r):
    u = find(u, p)
    v = find(v, p)
    if r[u] > r[v]:
        tmp = u
        u = v
        v = tmp
    p[u] = v
    if r[u] == r[v]:
        r[v] += 1

def kruskal(edges, N, p, r):
    edges.sort(key=lambda k: (k[2], k[0], k[1]))

    MST = []
    for edge in edges:
        u = edge[0]
        v = edge[1]
        if find(u, p) != find(v, p):
            MST.append(edge)
            union(u, v, p, r)
    return MST

if __name__ == '__main__':
    N, M = list(map(int, input().split()))

    edges = []
    for i in range(M):
        X, Y, L = list(map(int, input().split()))
        edges.append([X-1, Y-1, L, i])

    p = [i for i in range(N)]
    r = [1 for i in range(N)]
    MST = kruskal(edges, N, p, r)

    sum = 0
    for i in range(0, len(MST)):
        sum += MST[i][2]
    print(sum)
    for i in range(0, len(MST)):
        edge = MST[i]
        print(edge[0]+1, edge[1]+1)