import sys

n = int(input())
num_list = list(map(int, sys.stdin.readline().split()))

max = num_list[0]
min = num_list[0]

for i in num_list:
  if i > max:
    max = i
  elif i < min:
    min = i

print(min, max)


# 빠른 풀이, 파이썬 내장함수 이용
#print(min(num_list), max(num_list), end="")