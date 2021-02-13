import sys
sys.setrecursionlimit(1000000)

n, ｍ = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]

def dfs(v, p = -1):
	# v から行ける各頂点uを調べる。
    for u in to[v]:
        if u == p: continue　
        dfs(u, v)　# uが探索済でないなら、再起で探索する。

to = [list() for _ in range(n+1)]
for a, b in AB:
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

dfs(0)
