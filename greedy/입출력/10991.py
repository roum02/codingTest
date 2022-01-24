n = int(input())

for i in range(1,n+1):
  str = " "*(n-i)
  for j in range(1,i+1):
    if i == j:
      str += "*"
    else:
      str += "* "
  print(str)
