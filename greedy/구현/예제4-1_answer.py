#답안이 맞는데 답이 안맞는 이유는??????ㅠㅠㅠ/???

n = 5
plans = ["R", "R", "R", "U", "D", "D"]

x, y = 1, 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
locations = ["L", "R", "U", "D"]

for plan in plans:
  for i in range(len(locations)):
    if plan == locations[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx <1 | nx > n | ny <1 | ny > n :
    continue
  x, y = nx, ny

print(x, y)
