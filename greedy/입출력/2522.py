n = int(input())

empty_list = [" " for i in range(n)]

for i in range(1,2*n):
  if i <= n:
    empty_list[-i] = "*"
    print("".join(empty_list))
  else:
    empty_list[i-(n+1)] = " "
    print("".join(empty_list))
