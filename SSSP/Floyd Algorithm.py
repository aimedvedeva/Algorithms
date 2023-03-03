import math

if __name__ == '__main__':
    n = int(input())

    d = [[math.inf for x in range(n)] for y in range(n)]
    for i in range(n):
        d[i][i] = 0

    arcs = []
    for i in range(n):
        weights = list(map(int, input().split(' ')))
        for j, w in enumerate(weights):
            if w != 0:
                arcs.append([i, j, w])

    for arc in arcs:
        d[arc[0]][arc[1]] = min(d[arc[0]][arc[1]], arc[2])

    for t in range(n):
        for u in range(n):
            for v in range(n):
                d[u][v] = min(d[u][v], d[u][t] + d[t][v])

    for line in d:
        line = [0 if i==math.inf else i for i in line]
        print(*line)