# 시각 -> 틀린 이유: 시간 중 3이 하나라도 들어가면 카운트
# 완전탐색알고리즘: 다 실현해봐야함. 

n = 5

h = 0
m = 0
s = 0
count = 0
times = ""

for h in range(n+1):
  for m in range(60):
    for s in range(60):
      times = str(h)+str(m)+str(s)
      #print(times)
      if "3" in times:
        count += 1
    times = ""

print(count)