from collections import deque

# n*m 크기, 출구 (n,m)
n,m = 5, 6

graph = [
 [1,0,1,0,1,0],
 [1,1,1,1,1,1],
 [0,0,0,0,0,1],
 [1,1,1,1,1,1],
 [1,1,1,1,1,1]
]

# 위치(1,1)

# 괴물 있으면 0, 괴물 없으면 1
# 탈출하기 위해 움직여야하는 최소 칸의 개수? 

# 탈출하기 위해: x+1 or y+1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

  return graph[n-1][m-1]

print(bfs(0,0))
