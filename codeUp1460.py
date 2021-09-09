def solution(n):
  inner = []
  outer = []
  c = 0

  for i in range(1,n+1):
    inner.append(i+c)
    for i in range(1, n+1):
      outer.append(inner)
    c += 3
  return outer

print(solution(3))
