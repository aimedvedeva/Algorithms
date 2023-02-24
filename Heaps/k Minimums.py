def heapify(arr, pos, n):
    while (2 * pos + 1 < n):
        c = 2 * pos + 1
        if (c + 1 < n and arr[c + 1] > arr[c]):
            c += 1
        if arr[c] > arr[pos]:
            swap(arr, c, pos)
            pos = c
        else:
            break

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

a1 = 0
a0 = 0
A = 0
B = 0
C = 0
M = 0

def generateValue(a_i_2, a_i_1, i):
    global a0, a1, A, B, C, M
    if i == 0:
        return a0
    elif i == 1:
        return a1
    return (A * a_i_2 + B * a_i_1 + C) % M

def getKMins(l, r, k):
    heap = []

    a0 = 0
    a1 = 0

    for i in range(0, r+1):

        tmp = generateValue(a0, a1, i)
        a0 = a1
        a1 = tmp

        if i >= l:
            if len(heap) < k:
                heap = [tmp] + heap
                heapify(heap, 0, len(heap))

            elif heap[0] > tmp:
                heap[0] = tmp
                heapify(heap, 0, len(heap))

    heap.sort(reverse=False)
    return heap

if __name__ == '__main__':

    a0, a1, A, B, C, M = [int(i) for i in input().split(' ')]
    l, r, k = [int(i) for i in input().split(' ')]

    result = getKMins(l, r, k)

    print(*result)