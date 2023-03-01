import collections
import math

def possiblePositions(x, n):
    return [(x+1)%n, (x*x+1)%n, (x*x*x+1)%n]

if __name__ == '__main__':
    n, a, b = list(map(int, input().split(' ')))
    steps = []

    queue = collections.deque()
    queue.append(a)
    dists = dict()
    dists[a] = 0
    parents = dict()
    parents[a] = a

    while queue.__len__() != 0:
        cur_x = queue.popleft()
        for position in possiblePositions(cur_x, n):
            if dists.get(position, math.inf) == math.inf:
                dists[position] = dists[cur_x] + 1
                parents[position] = cur_x
                queue.append(position)

    if dists.get(b, math.inf) == math.inf:
        print(-1)
    else:
        path = [b]

        pos = b
        while (pos != a):
            path.append(parents.get(pos))
            pos = parents.get(pos)


        print(dists[b])

        print(*path[::-1])

