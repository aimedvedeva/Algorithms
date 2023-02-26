import math

def query(l, r, K, a, blocksums):
    sum = 0
    i = l
    while i < min(r+1, len(a)):
        if (i % K == 0 and i + K <= r + 1):
            sum += blocksums[i // K]
            i += K
        else:
            sum += a[i]
            i += 1
    return sum

def assign(a, a_id, val, K, blocksums):
    blocksums[a_id // K] -= a[a_id]
    a[a_id] = val
    blocksums[a_id // K] += a[a_id]

def createBlocksums(a, K, res):
    blocksums = [0] * (K + res)

    for block_id in range(len(blocksums)):
        l = block_id*K
        r = (block_id+1)*K
        blocksums[block_id] = sum(a[block_id*K : min((block_id+1)*K, len(a))])

    return blocksums

def RSQ(a, blocksums, ops, K):

    for op in ops:
        if op[0] == 1:
            a_id = op[1]-1
            new_val = op[2]
            assign(a, a_id, new_val, K, blocksums)
        else:
            l = op[1]-1
            r = op[2]-1
            lr_sum = query(l, r, K, a, blocksums)
            print(lr_sum)

if __name__ == '__main__':
    n, m = list(map(int,input().split(' ')))
    a = list(map(int,input().split(' ')))
    ops = []
    for i in range(m):
        ops.append(list(map(int, input().split(' '))))

    K = math.sqrt(len(a))
    if K == int(K):
        res = 0
    else:
        res = 1
    K = round(K)

    blocksums = createBlocksums(a, K, res)
    RSQ(a, blocksums, ops, K)
