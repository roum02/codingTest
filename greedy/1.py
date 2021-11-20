# 거스름돈 문제 해결 아이디어
# 해결: 가장 큰 화폐 단위부터 거슬러준다. 
# 다만, 이것이 정당한지 검토함이 필요 

n = 1260
count = 0

# O(n)
array = [500, 100, 50, 10]

for coin in array:
  count+= n//coin
  n %= coin

print(count)


