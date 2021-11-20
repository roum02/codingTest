# N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 수행
# 1.N에서 1빼기
# 2.N을 K로 나누기 : N이 K로 나누어 떨어질때만 가능

# N이 1이 될때까지 1번 혹은 2번의 과정을 수행해야 하는 최소

def solution(N, K):
  count = 0
  num = N

  while (num > 1):
    if num%K == 0 :
      num = num//K
      count += 1
    else:
      num = num-1
      count += 1

  return print(num, count)

#solution(25,3)


# 문제 해결 아이디어: N에 대하여 최대한 많이 나누기
# 1을 빼는 것 보다 나누는 것이 빨리 줄일 수 있음

# 답안 예시: Olog(n)시간 복잡도가 가능함!
n, k = map(int, input().split)
result = 0

while True:
  # n이 k로 나누어 떨어지지 않을 때 가장 가까운 나누어지는 수 구할 수 있음
  target = (n//k) * k
  # 연산을 수행하는 횟수
  result += (n - target)
  n = target

  if n < k:
    break
  result += 1
  n //= k

# 남은 수에 대해 1씩 빼기
result += (n-1)
print(result)