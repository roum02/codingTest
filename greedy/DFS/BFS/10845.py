import sys
from collections import deque

n = int(sys.stdin.readline().strip())
#n = int(input())
data = [sys.stdin.readline().strip() for i in range(n)]

queue = deque([])

for i in data:
  if 'push' in i:
    push_num = int(i[-1])
    queue.append(push_num)
    #print('push',queue)
  elif 'pop' in i:
    if queue:
      pop_num = queue.popleft()
      print(pop_num)
      #print('pop:', queue)
    else:
      print(-1)
      #print('pop:', queue)
  elif 'size' in i:
    print(len(queue))
    #print('size:', queue)
  elif 'empty' in i:
    if queue:
      print(0)
      #print('empty', queue)
    else:
      print(1)
      #print('empty', queue)
  elif 'front' in i:
    if not queue:
      print(-1)
    else:
      print(queue[0])
      #print('front', queue)
  elif 'back' in i:
    if not queue:
      print(-1)
    else:
      print(queue[-1])
      #print('back', queue)





