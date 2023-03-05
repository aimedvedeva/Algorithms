import sys
import threading

sys.setrecursionlimit(10**6)
threading.stack_size(10**8)

is_cyclic = False
start = 0
end = 0

def DFS(u, colors, adj_list, parents, parent):
    global is_cyclic, start, end

    colors[u] = 0
    parents[u] = parent
    for neighbour in adj_list[u]:
        if colors[neighbour] == -1:
            DFS(neighbour, colors, adj_list, parents, u)
        elif colors[neighbour] == 0:
            start = neighbour
            end = u
            is_cyclic = True
    colors[u] = 1

def run():
    global start, end, is_cyclic
    q = int(input())

    data = []
    for i in range(q):
        n, m  = list(map(int, input().split(' ')))

        adj_list = [[] for y in range(n)]

        for i in range(m):
            a, b = list(map(int, input().split(' ')))
            adj_list[a-1].append(b-1)

        data.append((n, adj_list))


    cyclicity_check = []

    for i in range(q):
        is_cyclic = False
        adj_list = data[i][1]
        n = data[i][0]

        colors = [-1] * n
        # -1 - white
        # 0 - gray
        # 1 - black
        parents = [-1] * n

        for j in range(n):
            if colors[j] == -1:
                DFS(j, colors, adj_list, parents, j)

        if is_cyclic:
            cycle = []
            while (start != end):
                cycle.append(end+1)
                end = parents[end]
            cycle.append(start+1)
            cyclicity_check.append((is_cyclic, cycle))
        else:
            cyclicity_check.append((is_cyclic, []))

    for item in cyclicity_check:
        if item[0] == True:
            cycle = item[1]
            print("NO")
            print(len(cycle))
            cycle = cycle[::-1]
            cycle.append(cycle[0])
            print(*cycle)
        else:
            print("YES")

threading.Thread(target=run).start()