n = int(input())

for i in range(1, n+1):
  if i == 1 or i == n:
    str = (" "*(n-i)) + ("*"*(2*i-1))
    print(str)
  else:
    str = (" "*(n-i)) + "*" + (" "* (2*(i-1)-1) + "*")
    print(str)