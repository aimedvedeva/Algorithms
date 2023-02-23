def heapify(arr, pos, n):
    while (2 * pos + 1 < n):
        c = 2 * pos + 1
        if (c + 1 < n and arr[c + 1][0] < arr[c][0]):
            c += 1
        if arr[c][0] < arr[pos][0]:
            swap(arr, c, pos)
            pos = c
        else:
            break

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def buildHeap(arr):
    for i in range(len(arr)-1, -1, -1):
        heapify(arr, i, len(arr))
    return arr

def mergeAPs(APs, k):
    result = []

    heap = []

    for AP in APs:
        heap.append((AP[0], AP[1]))
    heap = buildHeap(heap)

    while len(result) < k:

        min = heap[0]
        result.append(min[0])

        min_AP_element = min[0]
        min_AP_diff = min[1]

        heap[0] = (generateAP(min_AP_element, min_AP_diff), min_AP_diff)
        heapify(heap, 0, len(heap))

    return result

def generateAP(first, diff):
    return first + diff

if __name__ == '__main__':
    n = int(input())
    APs = []
    for i in range(n):
        APs.append(list(map(int, input().split(' '))))
    k = int(input())

    result = mergeAPs(APs, k)

    print(*result)