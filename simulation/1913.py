# 아이디어
# 1)가로, 세로 n인 이중 리스트 만들기: 0으로 채우기
# 현재 위치값: x, y
#while 1:
# 0일 경우에만 채우기
# 2) 0부터 n-1까지 -1씩 빼면서 세로 내려오기
#     map[0][0]: n^2, map[0][1]: n^2-1, map[0][2]: n^2-2
# 3) n-1까지 왔다면 다시 y:현재위치 x:0부터 n-1까지 -1씩 빼면서 가기
# 4) x가 n-1까지 왔다면 다시 y:현재위치 ~ n-1까지 -1씩 빼면서 가기
# 5)안에 있는 숫자가 1이되면 break 

# dx, dy 설정, 처음 d값은 1

# d방향으로 간다
# 앞이 벽이거나 0이 아니면 방향을 바꾼다(남->동->북->서)

import sys
input = sys.stdin.readline

n = int(input())
findNum = int(input())

map = [[0 for _ in range(n)] for _ in range(n)]
x, y = 0, 0
# 남동북서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
currentNum = n*n

while 1:
  if map[y][x] == 0:
    map[y][x] = currentNum
    if findNum == currentNum:
      findX, findY = x, y
    currentNum -= 1

  for i in range(0,4):
    nx = x + dx[d]
    ny = y + dy[d]

    if 0<=nx<n and 0<=ny<n:
      if map[ny][nx] == 0:
        x = nx
        y = ny
        break
        
      else:
        d = (d +1)%4
        break
    else:
        d = (d +1)%4
        break
  
  if currentNum == 0:
    break
  
for i in range(0, n):
  for j in range(0, n):
    print(map[i][j], end=" ")
  print("")
print(findY+1, findX+1)



