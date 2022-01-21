# n * m

n, m = 4, 5

graph = [
  [0,0,1,1,0],
  [0,0,0,1,1],
  [1,1,1,1,1],
  [0,0,0,0,0]
]

# 방문했는지 알기 위함
is_visited = [[0]*m for _ in range(n)]

# 얼음의 현재 위치
x, y = 0,0

def solution(graph, x, y):
  # 범위 지정
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False

  if graph[x][y] == 0:
    graph[x][y] = 1
    solution(graph, x-1, y)
    solution(graph, x+1, y)
    solution(graph, x, y-1)
    solution(graph, x, y+1)
    return True
  return False


result = 0

for i in range(n):
  for j in range(m):
    if solution(graph, i, j) == True:
      result += 1

print(result)
