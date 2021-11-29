#모험가 n명, 공포도 높으면 대처도 떨어짐
#공포도가 X인 모함가는 반드시 X명 이상 구성한 그룹에 참여
#여행 떠날 수 있는 그룹 수의 최대값

n = 5
arr = [2,3,1,2,2]
count = 0

arr.sort()
print(arr) #[1, 2, 2, 2, 3]
#new_arr = arr

for i in range(len(arr)):
  #new_arr = [x for x in arr if x not in arr[:new_arr[i]]]
  for j in range(i+1, arr[i]):
    if arr[i] < arr[j]:
      break
    else:
      count += 1
      i += arr[i]
    print(i)

print(count)

## 풀이
## 한 줄에 공백을 기준으로 입력
n = int(input())
data = list(map(int, input.split()))
data.sort()

result = 0 #총 그룹 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)

  
