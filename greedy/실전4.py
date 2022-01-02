# 1이 될 때까지

# n이 1이 될 때까지 1.n-1 2.n/k(n%k == 0 일때) 반복
# 최소 횟수 구하기

# n, k = map(int, input().split())
n, k = 27, 3

count = 0

#나눠야 하는 count
# while n > 0:
#   if n == 1:
#      break
#   n = n - ((n - (n//k*k)) * 1)
#   #빼야 하는 count
#   count = count + ((n - ((n//k)*k)))
#   print("빼기",n, count)
#   if n%k ==0:
#     n = n/k
#     count += 1
#     print("나누기",n, count)
#     if n == 1:
#       break

while n > 0:
  if n%k != 0:
    if (n//k) == 0:
      count += 1
      n = n - 1
    else: 
      count += n - ((n//k)*k)
      n = ((n//k)*k)
    print("빼기:",n, count)
    if n == 1:
      break
  elif n%k == 0:
    n = n/k
    count += 1
    print("나누기:",n, count)
    if n == 1:
      break
    

print(int(n), count)
    
