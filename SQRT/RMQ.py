import math

def assign(a, a_id, val, K, blockmins):
    id = a_id // K
    blockmins[id] = math.inf
    a[a_id] = val

    i = id * K
    while i < min((id+1)*K, len(a)):
        blockmins[id] = min(blockmins[id], a[i])
        i += 1

def getMin(l, r, K, a, blockmins):
    lr_min = math.inf

    i = l
    while i < min(r+1, len(a)):
        if (i % K == 0  and i + K <= r + 1):
            block_id = i // K
            lr_min = min(blockmins[block_id], lr_min)
            i += K
        else:
            lr_min = min(a[i], lr_min)
            i += 1

    return lr_min

def createBlockmins(a, K, res):
    blockmins = [math.inf] * (K+res)

    for id, val in enumerate(a):
        block_id = id // K
        blockmins[id // K] = min(blockmins[id // K], a[id])

    return blockmins

def RMQ(a, blockmins, ops, K):

    for op in ops:
        if op[0] == 1:
            a_id = op[1]-1
            new_val = op[2]
            assign(a, a_id, new_val, K, blockmins)
        else:
            l = op[1]-1
            r = op[2]-1
            lr_min = getMin(l, r, K, a, blockmins)
            print(lr_min)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split(' ')))
    m = int(input())
    ops = []
    for i in range(m):
        ops.append(list(map(int, input().split(' '))))

    K = math.sqrt(len(a))
    if K == int(K):
        res = 0
    else:
        res = 1
    K = round(K)

    blockmins = createBlockmins(a, K, res)
    RMQ(a, blockmins, ops, K)
