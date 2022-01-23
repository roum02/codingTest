x, y = map(int, input().split())

# n월의 마지막이 무슨 요일인지
# 그 요일+1요일에 따라 해당 월의 요일이 결정된다

if x == 1 or x == 10:
  if y%7 == 1:
    print("MON")
  elif y%7 == 2:
    print("TUE")
  elif y%7 == 3:
    print("WED")
  elif y%7 == 4:
    print("THU")
  elif y%7 == 5:
    print("FRI")
  elif y%7 == 6:
    print("SAT")
  elif y%7 == 0:
    print("SUN")
# 1월 31일은 수요일, 2월 1일은 목요일
# 2월 28일은 수요일, 3월 1일은 목요일
elif x == 2 or x == 3 or x == 11:
  if y%7 == 1:
    print("THU")
  elif y%7 == 2:
    print("FRI")
  elif y%7 == 3:
    print("SAT")
  elif y%7 == 4:
    print("SUN")
  elif y%7 == 5:
    print("MON")
  elif y%7 == 6:
    print("TUE")
  elif y%7 == 0:
    print("WED")
# 3월 31일은 토요일, 4월 1일은 일요일
elif x == 4 or x == 7:
  if y%7 == 1:
    print("SUN")
  elif y%7 == 2:
    print("MON")
  elif y%7 == 3:
    print("TUE")
  elif y%7 == 4:
    print("WED")
  elif y%7 == 5:
    print("THU")
  elif y%7 == 6:
    print("FRI")
  elif y%7 == 0:
    print("SAT")
# 4월 30일은 월요일, 5월 1일은 화요일
elif x == 5:
  if y%7 == 1:
    print("TUE")
  elif y%7 == 2:
    print("WED")
  elif y%7 == 3:
    print("THU")
  elif y%7 == 4:
    print("FRI")
  elif y%7 == 5:
    print("SAT")
  elif y%7 == 6:
    print("SUN")
  elif y%7 == 0:
    print("MON")
# 5월 31일은 목요일, 6월 1일은 금요일
elif x == 6:
  if y%7 == 1:
    print("FRI")
  elif y%7 == 2:
    print("SAT")
  elif y%7 == 3:
    print("SUN")
  elif y%7 == 4:
    print("MON")
  elif y%7 == 5:
    print("TUE")
  elif y%7 == 6:
    print("WED")
  elif y%7 == 0:
    print("THU")
# 6월 30일은 토요일, 7월 1일은 일요일
# 7월 31일은 화요일, 8월 1일은 수요일
elif x == 8:
  if y%7 == 1:
    print("WED")
  elif y%7 == 2:
    print("THU")
  elif y%7 == 3:
    print("FRI")
  elif y%7 == 4:
    print("SAT")
  elif y%7 == 5:
    print("SUN")
  elif y%7 == 6:
    print("MON")
  elif y%7 == 0:
    print("TUE")
# 8월 31일은 금요일, 9월 1일은 토요일
elif x == 9 or x == 12:
  if y%7 == 1:
    print("SAT")
  elif y%7 == 2:
    print("SUN")
  elif y%7 == 3:
    print("MON")
  elif y%7 == 4:
    print("TUE")
  elif y%7 == 5:
    print("WED")
  elif y%7 == 6:
    print("THU")
  elif y%7 == 0:
    print("FRI")
# 9월 30일은 일요일, 10월 1일은 월요일
# 10월 31일은 수요일, 11월 1일은 목요일
# 11월 30일은 금요일, 12월 1일은 토요일