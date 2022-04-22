# 로봇청소기 청소 영역의 개수 구하기
# 장소 N*M, 각 칸은 벽 또는 빈칸
# 청소기는 동서남북 중 하나를 바라보고 있음
# 지도의 북쪽에서 r번째, 서쪽에서 c번째 칸은 (r,c)

# 1. 현재위치 탐색 
# 2. 다음을 반복하며 인접 위치 탐색 
#   a) 왼쪽 청소 안했으면 왼쪽으로 회전하고 한칸 전진, 1번으로 돌아감. 그렇지 않으면 왼쪽 방향으로 회전(현재 바라보는 방향 기준으로 왼쪽)
#   b) 1번으로 돌아가거나 후진하지않고 2a가 연속 4번 실행되었을 경우, 바로 뒤쪽이 벽이면 작동 멈추기. 그렇지 않다면 한 칸 후진

# 첫째줄 세로 N, 가로 M
# 둘째줄 좌표(r,c)와 방향d
# 셋째줄 빈칸0, 벽1



# ### 1.아이디어 떠올리기
# 	1) 특정 조건으로 멈추지 않는 이상 계속 작동: while문
#     2) 방향 4가지 탐색: for문
#     3) 4방향 안됨: 후진
#     4) 후진도 안됨: break
    
# ### 2.시간복잡도 
#     1) 최대 N * M O(NM)
#     2) 각 4번씩 회전
    
# ### 3.자료구조: 시뮬레이션은 복잡도를 낮추는 것이 중요
#     1) 전체 지도: int[][]
#     	- 0: 청소x, 1:벽, 2: 청소o
#     2) 내위치(y,x), 방향(d): int, int, int
#     3) 전체 청소한 개수 count: int



## 입력값 외우기! ## 
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while True:
  # 현재위치 청소
  if map[y][x] == 0:
    map[y][x] = 2
    cnt += 1
    sw = False

  for i in range(1,5):
    # 다음에 바라볼 곳 ny, nx
    ny = y + dy[d-i]
    nx = x + dx[d-i]

    # 2차원 백터에서 다음을 탐색할 때, 항상 범위 안에 있는지 체크
    if 0<=nx<M and 0<=ny<N:
      if map[ny][nx] == 0:
        d = d-i
        y = dy
        x = dx
        # 다시 1 번으로 돌아감
        sw = True 
        break
      
      # 4방향 모두 있지 않은 경우: sw가 False일때만 오게끔
      if sw == False:
        # 뒤쪽 방향이 막혀있는지 확인
        ny = y - dy[d]
        nx = x - dx[d]

        if 0<=nx<M and 0<=ny<N:
          if map[dy][dx] == 1:
            break
          else:
            y = dy
            x = dx
            # 2번으로 돌아가야함!
        else:
          break

print(cnt)