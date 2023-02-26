import math

def buildSegmentTree(v, l, r, T, a):
    if l == r:
        T[v] = a[l]
    else:
        m = (l + r) // 2
        next_v = 2 * v + 1
        buildSegmentTree(next_v, l, m, T, a)

        buildSegmentTree(next_v + 1, m + 1, r, T, a)
        T[v] = min(T[2 * v + 1], T[2 * v + 2])

def change(v, l, r, x, t, T):
    if l == r:
        T[v] = t
    else:
        m = (l + r) // 2
        if x <= m:
            change(2 * v + 1, l, m, x, t, T)
        else:
            change(2 * v + 2, m+1, r, x, t, T)
        T[v] = min(T[2 * v + 1], T[2 * v + 2])

def getmin(v, l, r, L, R, T):
    if R < l or L > r:
        return math.inf
    if l >= L and r <= R:
        return T[v]
    m = (l + r) // 2
    return min(getmin(2 * v + 1, l, m, L, R, T), getmin(2 * v + 2, m + 1, r, L, R, T))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split(' ')))
    m = int(input())
    ops = []
    for i in range(m):
        ops.append(list(map(int, input().split(' '))))

    T = [math.inf]*(4*(len(a)-1))
    buildSegmentTree(0, 0, len(a)-1, T, a)

    for op in ops:
        if op[0] == 1:
            id = op[1]-1
            new_val = op[2]
            change(0, 0, len(a)-1, id, new_val, T)
        else:
            L = op[1]-1
            R = op[2]-1
            LR_sum = getmin(0, 0, len(a)-1, L, R, T)
            print(LR_sum)
