from queue import Empty


n = int(input())

empty_list = ["*" for i in range(n)]

for i in range(n):
  if i-1 >= 0:
    empty_list[i-1] = " "
  print("".join(empty_list))