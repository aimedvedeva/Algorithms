import math

if __name__ == '__main__':
    n, m = list(map(int, input().split(' ')))

    arcs = []

    for i in range(m):
        a, b, w = list(map(int, input().split(' ')))
        arcs.append([a-1, b-1, w])

    d = [math.inf] * n
    d[0] = 0

    parents = [-1] * n
    parents[0] = 0

    for i in range(n-1):
        for arc in arcs:
            u = arc[0]
            v = arc[1]
            w = arc[2]
            if d[u] < math.inf and d[v] > d[u] + w:
                d[v] = d[u] + w
                parents[v] = u

    t = ["NO" if i==math.inf else i for i in d]
    print(*t[1:])



