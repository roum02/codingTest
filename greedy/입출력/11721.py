# 한 줄에 10글자씩 끊어서 입출력

str = input()

start = 0

while True:
  print(str[start:start+10])
  str = str[start+10:]
  if len(str) <= 0:
    break
