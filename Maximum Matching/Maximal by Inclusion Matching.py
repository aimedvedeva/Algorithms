
def maxMatching(A, m, n):
    M = [-1 for i in range(m)]
    used = [False] * n
    for vertex, adj_list in enumerate(A):
        tryKhun(vertex, used, A, M)
    return M

def tryKhun(a, used, A, M):
    if used[a]:
        return False
    used[a] = True
    for b in A[a]:
        if M[b] == -1:
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

    M = maxMatching(A, m, n)

    print(sum(1 for i in M if i != -1))
    for b, a in enumerate(M):
        if a != -1:
            print(a+1, b+1)