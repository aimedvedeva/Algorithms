import math

def buildSegmentTree(v, l, r, T, a):
    if l == r:
        T[v] = a[l]
    else:
        m = (l + r) // 2
        next_v = 2 * v + 1
        buildSegmentTree(next_v, l, m, T, a)

        buildSegmentTree(next_v + 1, m + 1, r, T, a)
        T[v] = T[2 * v + 1] + T[2 * v + 2]

def change(v, l, r, x, t, T):
    if x < l or x > r:
        return
    if l == r:
        T[v] = t
    else:
        m = (l + r) // 2
        if x <= m:
            change(2 * v + 1, l, m, x, t, T)
        else:
            change(2 * v + 2, m+1, r, x, t, T)
        T[v] = T[2 * v + 1] + T[2 * v + 2]

def getsum(v, l, r, L, R, T):
    if R < l or L > r:
        return 0
    if l >= L and r <= R:
        return T[v]
    m = (l + r) // 2
    return getsum(2 * v + 1, l, m, L, R, T) + getsum(2 * v + 2, m + 1, r, L, R, T)

if __name__ == '__main__':
    n, m = list(map(int,input().split(' ')))
    a = list(map(int,input().split(' ')))
    ops = []
    for i in range(m):
        ops.append(list(map(int, input().split(' '))))

    T = [0]*(4*len(a))
    buildSegmentTree(0, 0, len(a)-1, T, a)

    for op in ops:
        if op[0] == 1:
            id = op[1]-1
            new_val = op[2]
            change(0, 0, len(a)-1, id, new_val, T)
        else:
            L = op[1]-1
            R = op[2]-1
            LR_sum = getsum(0, 0, len(a)-1, L, R, T)
            print(LR_sum)
