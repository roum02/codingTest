#모험가 n명, 공포도 높으면 대처도 떨어짐
#공포도가 X인 모함가는 반드시 X명 이상 구성한 그룹에 참여
#여행 떠날 수 있는 그룹 수의 최대값

n = 5
arr = [2,3,1,2,2]
count = 0

arr.sort()
new_arr = arr

i = 0
while i<len(new_arr):
  new_arr = [x for x in arr if x not in arr[:new_arr[i]]]
  print(new_arr)
  print(new_arr[:new_arr[i]])
  i += 1