from collections import deque

n,m = map(int, input().split())
arr = [list(map(int,input())) for _ in range(n)]
#split 붙이면 공백 기준으로 입력받음
#그래서 입력에 띄어쓰기 있으면 쓰고 
#없으면 input()만 쓰면 됨

#우 하 좌 상 순서대로 확인
#1일 경우에 이동 and 그 칸을 0으로 바꾸고 count+=1
#0일 경우에 이동안함

#이동할 네 방향 정의(상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  #큐 구현을 위해 deque 라이브러리 사용
  queue = deque()
  queue.append((x,y))
  #큐가 빌 때까지 반복
  while queue:
    x,y = queue.popleft()
    #현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      #미로 찾기 공간을 벗어난 경우 무시
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      #벽인 경우 무시
      if arr[nx][ny] == 0:
        continue
      #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if arr[nx][ny] == 1:
        arr[nx][ny] = arr[x][y]+1
        queue.append((nx,ny))
  return arr[n-1][m-1]
      
print(bfs(0,0))