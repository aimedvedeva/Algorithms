
def try_kuhn(vertex, visited_1, visited_2, part_1, mm_2_1, mm_1_2):
    if visited_1[vertex]:
        return False
    visited_1[vertex] = True

    for neighbour in part_1[vertex]:
        visited_2[neighbour] = True
        if mm_2_1[neighbour] == -1 or try_kuhn(mm_2_1[neighbour], visited_1, visited_2, part_1, mm_2_1, mm_1_2):
            mm_2_1[neighbour] = vertex
            mm_1_2[vertex] = neighbour
            return True
    return False


if __name__ == '__main__':
    n_1, n_2 = list(map(int, input().split()))

    part_1 = [[] for i in range(n_1)]

    for i in range(1, n_1+1):
        vertices_from_2 = list(map(int, input().split()))
        K = vertices_from_2[0]
        vertices_from_2 = vertices_from_2[1:]

        for vertex in vertices_from_2:
            part_1[i-1].append(vertex-1)

    mm_1_2 = list(map(lambda x: int(x)-1, input().split()))

    mm_2_1 = [-1 for i in range(n_2)]
    for i in range(n_1):
        idx = mm_1_2[i]
        vertex = i
        if idx != -1:
            mm_2_1[idx] = vertex

    visited_1 = [False] * n_1
    visited_2 = [False] * n_2
    for vertex, value in enumerate(mm_1_2):
        if value == -1:
            try_kuhn(vertex, visited_1, visited_2, part_1, mm_2_1, mm_1_2)

    print(sum(map(lambda x: x == False, visited_1)) + sum(map(lambda x: x == True, visited_2)))
    print(sum(map(lambda x: x == False, visited_1)), *[idx+1 for idx, value in enumerate(visited_1) if value == False])
    print(sum(map(lambda x: x == True, visited_2)), *[idx+1 for idx, value in enumerate(visited_2) if value == True])
