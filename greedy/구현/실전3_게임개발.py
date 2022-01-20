# 정사각형 n * m

n, m = 4, 4
x, y, direction = 1, 1, 0
# map
real_map = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]

# 방문했는지를 알기 위한 초기화 map
# is_visited = []
# for i in range(len(real_map)):
#   temp_list = []
#   for j in range(len(real_map)):
#     temp_list.append(0)
#   is_visited.append(temp_list)
#print(is_visited)

# 초기화 map 이렇게 줄여쓰기
is_visited = [[0]*m for i in range(n)]
is_visited[x][y] = 1 # 현재 위치 1로 표시

# dx, dy 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

turn_time = 0
count = 1
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전 후 안 가봤을 경우 + 갈 수 있는 경우
  if is_visited[nx][ny] == 0 and real_map[nx][ny] == 0:
    is_visited[nx][ny] = 1
    x = nx
    y = ny
    turn_time = 0
    count += 1
  # 회전 후 가봤을 경우 + 갈 수 없는 경우
  else:
    turn_time += 1

  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if real_map[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0

print(count)


  

