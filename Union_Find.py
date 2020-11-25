import sys

sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]

root = [-1] * n

def find(x):
    if root[x] < 0:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def unite(x, y):
    gx = find(x)
    gy = find(y)

    if gx == gy:
        return

    if root[gx] > root[gy]:
        gx, gy = gy, gx

    root[gx] += root[gy]
    root[gy] = gx

def size(x):
    x = find(x)
    return -root[x]

for a, b in AB:
    a -= 1
    b -= 1
    unite(a, b)

par = [i for i, x in enumerate(root) if x < 0]
print(len(set(par))-1)