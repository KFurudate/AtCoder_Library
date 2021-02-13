from collections import deque
 
def bfs(sx, sy, gx, gy):
    f_inf = float('inf')
    dist = [[f_inf] * m for _ in range(n)]
 
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
 
    que = deque([])
    que.append((sx, sy))
    dist[sx][sy] = 0
 
    while que:
        p = que.popleft()
 
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
 
            if n > nx >= 0 and m > ny >= 0 and \
                    c[nx][ny] != '#' and \
                    dist[nx][ny] == f_inf:
                que.append((nx, ny))
                dist[nx][ny] = dist[p[0]][p[1]] + 1
 
    return dist[gx][gy]
 
n, m = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
c = [input() for _ in range(n)]
sx -= 1
sy -= 1
gx -= 1
gy -= 1
 
print(bfs(sx, sy, gx, gy))