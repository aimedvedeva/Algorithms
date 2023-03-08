import sys
import threading

sys.setrecursionlimit(10**6)
threading.stack_size(10**8)

def tryKhun(a, used, A, M):
    if used[a]:
        return False
    used[a] = True
    for b in A[a]:
        if (M[b] == -1) or tryKhun(M[b], used, A, M):
            M[b] = a
            return True
    return False

def printMM(max_matching):
    print(sum(1 for i in max_matching if i != -1))
    for b, a in enumerate(max_matching):
        if a != -1:
            print(a+1, b+1)

def run():
    n_1, n_2 = list(map(int, input().split()))

    part_1 = [[] for i in range(n_1)]

    for i in range(1, n_1+1):
        vertices_from_2 = list(map(int, input().split()))
        K = vertices_from_2[0]
        vertices_from_2 = vertices_from_2[1:]

        for vertex in vertices_from_2:
            part_1[i-1].append(vertex-1)

    mm_to_check = list(map(lambda x: int(x)-1, input().split()))

    M = [-1 for i in range(n_2)]
    for i in range(n_1):
        idx = mm_to_check[i]
        vertex = i
        if idx != -1:
            M[idx] = vertex

    M_cpy_to_cmp = M.copy()

    used = [False] * n_1
    for vertex, adj_list in enumerate(part_1):
        if mm_to_check[vertex] == -1:
            tryKhun(vertex, used, part_1, M)

    if M_cpy_to_cmp == M:
        print("YES")
    else:
        print("NO")
        printMM(M)


threading.Thread(target=run).start()