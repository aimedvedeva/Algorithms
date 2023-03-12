import math

def getMinWeightEdge(d, visited):
    min_weight = math.inf
    edge = []
    for to_vertex, (from_vertex, weight) in enumerate(d):
        if not visited[to_vertex]:
            if weight < min_weight:
                min_weight = weight
                edge = [to_vertex, from_vertex, min_weight]

    return edge

def prim(n, adj_list):
    visited = [False for i in range(n)]
    d = [[-1, math.inf] for i in range(n)]

    start = 0
    for neighbour, weight in enumerate(adj_list[start]):
        if weight != math.inf:
          d[neighbour] = [start, weight]
    visited[start] = True

    MST = []

    while sum(visited) < N:

        edge = getMinWeightEdge(d, visited)
        MST.append(edge)

        to_vertex = edge[0]
        visited[to_vertex] = True
        d[to_vertex] = [-1, math.inf]
        for i, (from_vertex, weight) in enumerate(d):
            if not visited[i]:
                from_vertex, weight = d[i]
                if adj_list[to_vertex][i] < weight:
                    d[i] = [to_vertex, adj_list[to_vertex][i]]

    return MST

if __name__ == '__main__':
    N, M = list(map(int, input().split()))

    adj_list = [[math.inf for i in range(N)] for i in range(N)]
    for i in range(M):
        X, Y, L = list(map(int, input().split()))
        adj_list[X-1][Y-1] = L
        adj_list[Y-1][X-1] = L

    MST = prim(N, adj_list)


    sum = 0
    for i in range(0, len(MST)):
        sum += MST[i][2]
    print(sum)
    for i in range(0, len(MST)):
        edge = MST[i]
        print(edge[1]+1, edge[0]+1)