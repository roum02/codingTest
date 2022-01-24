n = int(input())

empty_list = [" " for i in range(2 * n)]

for i in range(1, 2*n):
  if i <= n:
    empty_list[i-1] = "*"
    empty_list[-i] = "*"
    print("".join(empty_list))
  else:
    empty_list[i-(2*i)] = " "
    empty_list[i-1] = " "
    print("".join(empty_list))