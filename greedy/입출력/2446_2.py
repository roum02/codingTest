n = int(input())

for i in range(2*n):
  if i < n:
    str = " "*i+"*"*(2*n-1-(2*i))
    print(str)
  elif i > n:
    str = " "*(2*n-1-i)+"*"*(2*i-2*n+1)
    print(str)