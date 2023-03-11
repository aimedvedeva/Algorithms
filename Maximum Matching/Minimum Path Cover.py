
def maxMatching(A, m, n):
    M = [-1 for i in range(m)]
    for vertex, adj_list in enumerate(A):
        used = [False] * n
        tryKhun(vertex, used, A, M)
    return M

def tryKhun(a, used, A, M):
    if used[a]:
        return False
    used[a] = True
    for b in A[a]:
        if (M[b] == -1) or tryKhun(M[b], used, A, M):
            M[b] = a
            return True
    return False


def getPath(M_A_B, a_vertex, visitedA, paths):
    new_path = []
    while True:
        new_path.append(a_vertex + 1)
        visitedA[a_vertex] = True
        a_vertex = M_A_B[a_vertex]
        if a_vertex == -1:
            break

    return new_path

def isPart(paths, path_to_check):
    is_part = False
    new_path_set = set(path_to_check)
    for i, path in enumerate(paths):
        if path != path_to_check:
            path_set = set(path)
            if new_path_set.issubset(path_set):
                is_part = True
    return is_part

if __name__ == '__main__':
    n, m = list(map(int, input().split()))

    adj_list = [[] for i in range(n)]

    for i in range(m):
        a, b = list(map(lambda x: int(x) - 1, input().split()))
        adj_list[a].append(b)

    M_B_A = maxMatching(adj_list, n, n)
    M_A_B = [-1 for i in range(n)]
    for i in range(n):
        idx = M_B_A[i]
        vertex = i
        if idx != -1:
            M_A_B[idx] = vertex

    paths = []
    visitedA = [False for i in range(n)]
    for a_vertex in range(n):
        if not visitedA[a_vertex]:
            path = getPath(M_A_B, a_vertex, visitedA, paths)
            paths.append(path)

    for vertex, flag in enumerate(visitedA):
        if not visitedA[vertex]:
            paths.append([vertex + 1])


    result = []
    for path in paths:
        if not isPart(paths, path):
            result.append(path)

    print(len(result))

    for path in result:
        if path is not None:
            print(*path)


