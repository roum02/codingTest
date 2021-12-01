#동, 북, 서, 남
# dx = [0,-1,0,1]
# dy = [1,0,-1,0]

# x, y = 2, 2

# for i in range(4):
#   # 다음 위치
#   nx = x + dx[i]
#   ny = y + dy[i]
#   print(nx, ny)


# n*n 크기 정사각형은 1*1로 나누어져 있음. 왼쪽 위(1,1) 오른 아래(n,n)
# 공간 밖은 무시, 도착 좌표?

n = int(input("n: "))
arr = input("arr: ").split(" ")

start = [1, 1]

for i in range(len(arr)):
  if arr[i] == "U":
    if 1 > start[0] -1:
      start[0] = 1
    else:
      start[0] = start[0] -1
  elif arr[i] == "D":
    if n < start[0] +1:
      start[0] = n
    else:
      start[0] = start[0] +1
  elif arr[i] == "L":
    if 1 > start[1] -1:
      start[1] = 1
    else:
      start[1] = start[1] -1
  elif arr[i] == "R":
    if n < start[1] +1:
      start[1] = n
    else:
      start[1] = start[1] +1
print(start)
