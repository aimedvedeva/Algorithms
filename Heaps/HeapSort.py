swaps = 0

def heapify(arr, pos, n):
    global swaps
    while (2 * pos + 1 < n):
        c = 2 * pos + 1
        if (c + 1 < n and arr[c + 1] > arr[c]):
            c += 1
        if arr[c] > arr[pos]:
            swap(arr, c, pos)
            swaps += 1
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

def HeapSort(arr):
    arr = buildHeap(arr)

    for i in range(len(arr) - 1, -1, -1):
        swap(arr, 0, i)
        heapify(arr, 0, i)
    return arr

if __name__ == '__main__':
    k = int(input())
    array = list(map(int, input().split(' ')))
    array = HeapSort(array)
    print(swaps)
    print(*array)