import math
def buildSegmentTreeSum(v, l, r, T, a):
    if l == r:
        T[v] = a[l]
    else:
        m = (l + r) // 2
        next_v = 2 * v + 1
        buildSegmentTreeSum(next_v, l, m, T, a)

        buildSegmentTreeSum(next_v + 1, m + 1, r, T, a)
        T[v] = T[2 * v + 1] + T[2 * v + 2]

def changeSum(v, l, r, x, t, T):
    if x < l or x > r:
        return
    if l == r:
        T[v] = t
    else:
        m = (l + r) // 2
        if x <= m:
            changeSum(2 * v + 1, l, m, x, t, T)
        else:
            changeSum(2 * v + 2, m+1, r, x, t, T)
        T[v] = T[2 * v + 1] + T[2 * v + 2]

def getsum(v, l, r, L, R, T):
    if R < l or L > r:
        return 0
    if l >= L and r <= R:
        return T[v]
    m = (l + r) // 2
    return getsum(2 * v + 1, l, m, L, R, T) + getsum(2 * v + 2, m + 1, r, L, R, T)

def change(v, l, r, x, t, T):
    if l == r:
        T[v][0] = t
    else:
        m = (l + r) // 2
        if x <= m:
            change(2 * v + 1, l, m, x, t, T)
        else:
            change(2 * v + 2, m+1, r, x, t, T)
        T[v] = argmin(T[2 * v + 1], T[2 * v + 2])

def argmin(pair1, pair2):
    if pair1[0] < pair2[0]:
        return pair1
    return pair2

def buildSegmentTree(v, l, r, T, a):
    if l == r:
        T[v] = a[l]
    else:
        m = (l + r) // 2
        next_v = 2 * v + 1
        buildSegmentTree(next_v, l, m, T, a)

        buildSegmentTree(next_v + 1, m + 1, r, T, a)
        T[v] = argmin(T[2 * v + 1], T[2 * v + 2])

if __name__ == '__main__':
    n = int(input())
    a = [[int(val), i] for i, val in enumerate(input().split(' '))]

    T = [math.inf]*(4*(len(a)-1))
    buildSegmentTree(0, 0, len(a)-1, T, a)

    b = [0] * len(a)
    Tb = [math.inf]*(4*(len(b)-1))
    buildSegmentTreeSum(0, 0, len(b)-1, Tb, b)

    n = len(a)
    while n > 0:
        old_id = T[0][1]

        new_id  = old_id - getsum(0, 0, len(b)-1, 0, old_id, Tb)
        # sum(b[0:old_id])
        print(new_id+1)

        changeSum(0, 0, len(b)-1, old_id, b[old_id] + 1, Tb)
        #b[old_id] += 1
        change(0, 0, len(a) - 1, old_id, math.inf, T)
        n -= 1

