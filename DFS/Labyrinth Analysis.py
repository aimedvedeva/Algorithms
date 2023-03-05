n = 0
m = 0
components_counter = 0

def generateSteps(i, j):
    global n, m
    return [(max(i-1, 0), j), (min(i+1, n-1), j), (i, max(j-1, 0)), (i, min(j+1, m-1))]

def DFS(i, j, map):
    global components_counter
    components_counter += 1

    map[i][j] = 1
    steps = generateSteps(i, j)
    for step in steps:
        if map[step[0]][step[1]] == -1:
            DFS(step[0], step[1], map)

if __name__ == '__main__':
    n, m = list(map(int, input().split(' ')))

    map = [[-1 for i in range(m)] for i in range(n)]

    for i in range(n):
        symbols = input()
        for j, symbol in enumerate(symbols):
            if symbol == '*':
                map[i][j] = -2

    # -1 - not visited
    # -2 - can't visit
    # 1 - visited
    components = []
    for i in range(n):
        for j in range(m):
            if map[i][j] == -1:
                DFS(i, j, map)
                components.append(components_counter)
                components_counter = 0

    print(len(components))
    components.sort()
    print(*components)


