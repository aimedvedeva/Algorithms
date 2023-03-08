def DFS(u, parents, adj_list, u_parent):
    parents[u] = u_parent
    for neighbour in adj_list[u]:
        if parents[neighbour] == -1:
            DFS(neighbour, parents, adj_list, u)

if __name__ == '__main__':
    n, a, b = list(map(int, input().split(' ')))

    adj_list = []

    for i in range(n):
        vertices = list(map(int, input().split(' ')))
        adj_line = []

        for id, vertex in enumerate(vertices):
            if id > i and vertex != 0:
                adj_line.append(id)

        adj_list.append(adj_line)

    parents = [-1] * n
    DFS(a - 1, parents, adj_list, -1)

    if parents[b-1] == -1:
        print("-1")
    else:
        path = []
        u = b-1
        while (u != a-1):
            path.append(u+1)
            u = parents[u]

        path = path + [a]

        print(len(path))
        print(*path)
