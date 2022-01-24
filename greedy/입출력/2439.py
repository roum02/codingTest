n = int(input())

empty_list = [" " for i in range(n)]

for i in range(n-1, -1, -1):
  empty_list[i] = "*"
  print("".join(empty_list))