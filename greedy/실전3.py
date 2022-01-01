# 숫자 카드 게임

# n,m = map(int, input().split())
# data = list(map(int, input().split))

n,m = 3, 3
data = [[3,1,2],[4,1,4],[2,2,2]]

max_value = 0


for i in data:
  if max_value < min(i):
    max_value = min(i)
  
print(max_value)