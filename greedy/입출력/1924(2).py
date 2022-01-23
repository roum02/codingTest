x, y = map(int, input().split())

# 누적되는 date에 %7하기

Day = 0
month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_list = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]

for i in range(x-1):
  Day += month_list[i]
Day = (Day+y)%7

print(week_list[Day])

