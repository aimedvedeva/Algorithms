def prefix(s):
    n = len(s)
    b = [0 for i in range(n)]
    for i in range(1, n):
        k = b[i - 1]
        while k > 0 and s[k] != s[i]:
            k = b[k - 1]
        if s[k] == s[i]:
            b[i] = k + 1
    return b


if __name__ == '__main__':
    s1 = input()
    s2 = input()

    result = prefix(s1 + '#' + s2)
    print(len(s1) - result[-1])
