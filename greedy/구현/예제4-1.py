#상하좌우: 개체를 상하좌우로 이동시킨다는 점에서 시뮬레이션 유형

n = 5
data = ["R", "R", "R", "U", "D", "D"]

# U이면 -1, D이면 +1, 1보다 작거나 n보다 크면 무시
upDown = 1
# L이면 -1, R이면 +1, 1보다 작거나 n보다 크면 무시
leftRight = 1

for i in data:
  if (i == "U") & (upDown > 1):
    upDown -= 1
  elif (i == "D") & (upDown < n):
    upDown += 1
  elif (i == "L") & (leftRight > 1):
    leftRight -= 1
  elif (i == "R") & (leftRight < n):
    leftRight += 1

print(upDown, leftRight)

