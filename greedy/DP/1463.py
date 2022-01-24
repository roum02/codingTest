# 1로 만드는 최소값 구하기

n = int(input())
count = 0
min = n

while True:
  if n == 1:
    break
  if n%3 == 0:
    if n/3 < min:
      min = int(n/3)
    n = min
  elif n%2 == 0:
    if n/2 < min:
      min = int(n/2)
    n = min
  else:
    n -= 1
  print(n)
    