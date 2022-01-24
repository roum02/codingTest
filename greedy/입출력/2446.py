n = int(input())

fulled_list = ["*" for _ in range(2*n-1)]

for i in range(2*n):
  if i == 0 :
    print("".join(fulled_list))
  
  elif i < n and i >0 :
    fulled_list[i-1] = " "
    fulled_list[-i] = " "
    print("".join(fulled_list))
  
  elif i > n:
    fulled_list[-i] = "*"
    fulled_list[i-1] = "*"
    print("".join(fulled_list))

