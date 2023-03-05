order = []
is_cyclic = False

def DFS(u, colors, adj_list, parents, parent):
    global is_cyclic, order

    colors[u] = 0
    parents[u] = parent
    for neighbour in adj_list[u]:
        if colors[neighbour] == -1:
            DFS(neighbour, colors, adj_list, parents, u)
        elif colors[neighbour] == 0:
            is_cyclic = True
    colors[u] = 1
    order.append(u)

if __name__ == '__main__':
    n, m = list(map(int, input().split(' ')))

    adj_list = [[] for i in range(n)]

    for i in range(m):
        a, b = list(map(int, input().split(' ')))
        adj_list[a].append(b)

    colors = [-1] * n
    # -1 - white
    # 0 - gray
    # 1 - black
    parents = [-1] * n

    for i in range(n):
        if colors[i] == -1:
            DFS(i, colors, adj_list, parents, i)

    if not is_cyclic:
        print("YES")
        print(*order[::-1])
    else:
        print("NO")