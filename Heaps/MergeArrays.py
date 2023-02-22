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

def mergeSortedArrays(arrays):
    result = []
    heap = []
    for idx, array in enumerate(arrays):
        heap.append((array[0], 0, idx))

    heap = buildHeap(heap)

    while len(heap) > 0:
        min = heap[0]
        result.append(min[0])
        try:
            array_idx = min[2]
            element_idx = min[1]
            heap[0] = (arrays[array_idx][element_idx+1], element_idx+1, array_idx)
        except:
            heap[0] = heap[-1]
            del heap[-1]
        heapify(heap, 0, len(heap))

    return result

if __name__ == '__main__':
    n = int(input())
    arrays = []
    for i in range(n):
        arrays.append(list(map(int, input().split(' ')))[1:])
    result = mergeSortedArrays(arrays)

    print(*result)