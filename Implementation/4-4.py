n,m = map(int, input().split())
a,b,direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * m for _ in range(n)]
d[a][b]=1 #현재 좌표 방문 처리
#d배열은 방문한 위치를 저장하기 위한 맵 배열
#arr배열은 바다인지 육지인지 구분해야하기에
#d배열을 따로 생성해줘야 겹치지 않음

dx = [0,0,-1,1]
dy = [-1,1,0,0]
#상하좌우
#북남서동
#0231
count=1
turn_time=0#돌아버린 횟수
#동남서북 -> 3210
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

while True:
  turn_left()#왼쪽으로 90도 도는 함수
  nx = a + dx[direction]
  ny = b + dy[direction]
  if arr[nx][ny] == 0 and d[nx][ny] == 0: #앞으로 간곳이 육지이고 방문하지 않은 곳이면
    d[nx][ny] = 1 #방문했다고체크해주고 
    a = nx #이동
    b = ny
    count+=1 #카운트해주고
    turn_time=0 #돌아버린 횟수 초기화
    continue #다음 코드들 실행안하고 위로 올라가서 다음 반복 실행
  else:
    turn_time+=1
  if turn_time == 4:#4번돌아버리면 원래 방향에서 뒤로가기
    nx = a - dx[direction]
    ny = b - dy[direction]
    if arr[nx][ny] == 0:#대신 육지여야 뒤로감
      a = nx
      b = ny
    else:
      break
    turn_time=0#뒤로 간 뒤에 돌아버린 횟수 초기화
print(count) 