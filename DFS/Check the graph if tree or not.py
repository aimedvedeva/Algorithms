
foundCycle = False

def DFS(u, visited, adj_list, parent_u):
    global foundCycle

    visited[u] = True

    for neighbour in adj_list[u]:
        if not visited[neighbour]:
            DFS(neighbour, visited, adj_list, u)
        else:
            if (neighbour != parent_u):
                foundCycle = True


if __name__ == '__main__':
    n = int(input())

    adj_list = []

    for i in range(n):
        vertices = list(map(int, input().split(' ')))
        adj_line = []
        for id, vertex in enumerate(vertices):
            if vertex != 0:
                adj_line.append(id)
        adj_list.append(adj_line)

    visited = [False] * n
    DFS(0, visited, adj_list, -1)

    if sum(visited) == n and not foundCycle:
        print("YES")
    else:
        print("NO")

