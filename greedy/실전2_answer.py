# 입력값 중 가장 큰 수와 두 번째로 큰 수를 저장하는 것이 포인트
# 가장 큰 수를 k번 더하고, 두 번째로 큰 수를 한 번 더하는 연산

#포인트2: 입력받은 리스트를 정렬하기!!


# n, m, k = map(int, input("숫자 입력: ").split())
# data = list(map(int, input("숫자 입력: ").split()))

n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]


data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)