
def Z(s):
    n = len(s)
    l = 0
    r = 0
    z = [0 for i in range(n)]

    for i in range(1, n):
        if r >= i:
            z[i] = min(z[i - l], r - i + 1)
        while z[i] + i < n and s[z[i]] == s[z[i] + i]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

if __name__ == '__main__':
    s = input()
    print(*Z(s))
