
#거슬러주어야 할 돈
#n = int(input("돈을 입력해주세요: "))

n = 1260
temp = n

#동전의 최소 개수
count = 0

while temp >= 0:
  if temp >= 500:
    c = temp//500
    temp = temp - (500*c)
    count += c
  if temp >= 100:
    c = temp//100
    temp = temp - (100*c)
    count += c
  if temp >= 50:
    c = temp//50
    temp = temp - (50*c)
    count += c
  if temp >= 10 :
    c = temp//10
    temp = temp - (10*c)
    count += c
  if temp == 0:
    break
print(temp, count)

