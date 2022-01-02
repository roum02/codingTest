#왕실의 나이트

# 8*8 좌표평면(행 a-h, 열 1-8)
#나이트 움직임: (1)수평2칸, 수직1칸 (-ㄱ) (2)수직2칸, 수평1칸 (L)
#위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수 
# 정원 밖으로는 못나감

location = 'c2'

#행
rows = ['a','b','c','d','e','f','g','h']
row = 0
count = 0

#오른쪽, 밑: +1
d1 = [[1,-2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2]]

for i in range(len(rows)):
  if rows[i] == location[:1]:
    row = i+1

x, y = row, int(location[-1])

print("x, y:", x,y)

for i in d1:
  nx = x + i[0]
  ny = y + i[1]
  if nx > 0 and ny > 0 and nx < 9 and ny < 9:
    count += 1
  # print(nx, ny, count)

print(count)