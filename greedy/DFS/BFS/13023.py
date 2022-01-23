from collections import deque
# 도시 1~n
# 단방향 도로 m개
# 특정 도시 x 에서 최단거리가 k인 모든 도시의 번호 출력

n, m, k, x = map(int, input().split())
graph = []
for i in range(m):
  graph.append(list(map(int, input().split())))

# stack에 이어지는 노드 쌓기
# 만약 최단거리가 아니라면 pass
# 길이가 k인 stack 개수 count

# stack = []
# start = 0
