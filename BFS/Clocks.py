import collections
import math

def possibleState(x, h, m):
    return [(x[0] + h) % 24, (x[1] + m) % 60]

if __name__ == '__main__':
    a1, b1, a2, b2 = list(map(int, input().split(' ')))
    h1, m1 = list(map(int, input().split(' ')))
    h2, m2 = list(map(int, input().split(' ')))

    queue = collections.deque()
    queue.append([h1, m1])
    parents = [[False for x in range(60)] for y in range(24)]
    dists = [[math.inf for x in range(60)] for y in range(24)]
    dists[h1][m1] = 0
    parents[h1][m1] = True

    while queue.__len__() != 0:
        cur_state = queue.popleft()
        states = []
        states.append(possibleState(cur_state, a1, b1))
        states.append(possibleState(cur_state, a2, b2))
        for state in states:
            if parents[state[0]][state[1]] == False:
                dists[state[0]][state[1]] = dists[cur_state[0]][cur_state[1]] + 1
                parents[state[0]][state[1]] = True
                queue.append(state)

    if dists[h2][m2] == math.inf:
        print(-1)
    else:
        print(dists[h2][m2])