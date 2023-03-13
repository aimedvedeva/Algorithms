
def get_length(u, p):
    return find(u, p)[1]

def find(u, p):
    if u == p[u]:
        return (u, 0)
    else:
        rep, len_from_p = find(p[u], p)
        p[u] = rep
        length[u] = len_from_p + length[u]
        return (rep, length[u])

def union(u, v, p):
    p[u] = v
    length[u] = 1

if __name__ == '__main__':
    n, m = list(map(int, input().split()))

    queries = []
    for i in range(m):
        data = list(map(int, input().split()))
        queries.append(data)

    p = [i for i in range(n)]
    length = [0] * n

    for query in queries:
        if query[0] == 1:
            # 1 a b => b is a boss for a
            a = query[1]-1
            boss = query[2]-1
            union(a, boss, p)
        elif query[0] == 2:
            # 2 c => depth of c
            c = query[1]-1
            print(get_length(c, p))
