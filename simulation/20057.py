# 아이디어
# 
# [모래]
# 1)현재위치x,y: n//2 
# 2)map[y][x-1] 모래값: currentSend, 
# 3)빠진 모래의 총 값: totalSend
# 4)밖으로 나간 모래의 값: outerSend
# 
# [토네이도] 
# 5)방향d(서0,남1,동2,북3), d%2 = 1 이면 tornado 하나씩 증가: d, tornado                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
# 6)dx = [-1,0,1,0], dy=[0,1,0,-1], * tornado: dx, dy
# 
# [계산식_회전]
# left = [(0,1,0.01),(0,-1,0.01),(-1,1,0.07),(-1,-1,0.07),(-1,2,0.02),(-1,-2,0.02),(-2,1,0.1),(-2,-1,0.1),(-2,0,0),(-3,0,0.05)]
# right = [(-x, y, z) for x,y,z in left]
# down = [(-y, x, z) for x,y,z in left]
# up = [(y, x, z) for x,y,z in left]
# 
# [계산식_함수]: 모래 계산이 목표
# params: x, y, direction
# 

# while true
# currentSend = map[y][x-1]
# if x,y가 0,n-1사이가 아닐 경우 outerSend에 담기
# 게산하기
# d = (d+1)%4
# if d%2 == 1이면 tornado += 1
# x += dx[d]*tornado, y += dy[d]*tornado

import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]



