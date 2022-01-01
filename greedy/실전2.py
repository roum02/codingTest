#큰 수의 법칙

# 배열의 크기 N, 숫자가 더해지는 횟수 M, K번 연속 불가

# n, m, k = map(int, input("숫자 입력: ").split())
# data = list(map(int, input("숫자 입력: ").split()))

n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]

max = 0
sub_max = 0
result = 0

for i in range(len(data)):
  if data[i] > max:
    max = data[i]

for i in range(len(data)):
  if (data[i] != max) & (data[i] > sub_max): 
    sub_max = data[i]
  
result += max * (m//k*k)
result += sub_max * (m-((m//k*k)))

print(result)

