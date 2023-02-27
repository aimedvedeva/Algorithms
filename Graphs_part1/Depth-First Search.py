def DFS(u, visited, adj_list, path, b):
    visited[u] = True

    # if u == b:
    #     return

    for neighbour in adj_list[u]:
        if not visited[neighbour]:
            path.append(neighbour + 1)
            DFS(neighbour, visited, adj_list, path, b)

            if path[-1] == b+1:
                return
            if path[-1] == (neighbour+1):
                del path[-1]




if __name__ == '__main__':
    n, a, b = list(map(int, input().split(' ')))

    adj_list = []

    for i in range(n):
        vertices = list(map(int, input().split(' ')))
        adj_line = []
        for id, vertex in enumerate(vertices):
            if vertex != 0:
                adj_line.append(id)
        adj_list.append(adj_line)

    visited = [False] * n
    path = [a]
    DFS(a - 1, visited, adj_list, path, b - 1)

    if path[-1] != b:
        print(-1)
    else:
        print(len(path) - 1)
        print(*path)