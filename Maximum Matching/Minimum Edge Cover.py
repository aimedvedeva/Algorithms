
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

if __name__ == '__main__':
    n, m = list(map(int, input().split()))

    A = [[] for i in range(n)]

    for i in range(1, n+1):
        B_vertices = list(map(int, input().split()))
        for vertex in B_vertices:
            if vertex != 0:
                A[i-1].append(vertex-1)

    M_B_A = maxMatching(A, m, n)

    visitedA = [False for i in range(n)]
    visitedB = [False for i in range(m)]

    edges = []

    for b, a in enumerate(M_B_A):
        if a != -1:
            visitedB[b] = True
            visitedA[a] = True
            edges.append([a+1, b+1])

    for a_vertex, adj_list in enumerate(A):
        for b_vertex in adj_list:
            if not visitedA[a_vertex] or not visitedB[b_vertex]:
                visitedA[a_vertex] = True
                visitedB[b_vertex] = True
                edges.append([a_vertex+1, b_vertex+1])

    print(len(edges))

    for i, value in enumerate(edges):
        print(value[0], value[1])
