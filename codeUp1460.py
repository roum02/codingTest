def solution(n):
  inner = []
  outer = []

  for i in range(1,n+1):
    inner.append(i)
    for i in range(1, n+1):
      outer.append(inner)
  return outer

print(solution(3))
