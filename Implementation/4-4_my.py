n,m = map(int, input().split())
a,b,direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
count = 1
d[a][b]=1
turn_time=0
#0123
#북동남서
def turn_left():
  global direction
  direction-=1
  if direction == -1:
    direction=3

while True:
  turn_left()
  nx = a + dx[direction]
  ny = b + dy[direction]
  if d[nx][ny] == 0 and arr[nx][ny] == 0:
    d[nx][ny]=1
    a, b = nx, ny
    count+=1
    turn_time=0
    continue
  else:
    turn_time+=1
  if turn_time==4:
    nx = a - dx[direction]
    ny = b - dy[direction]
    if arr[nx][ny]==0:
      a,b = nx,ny
    else:
      break # break문은 while문을 탈출시키도록함
    #break문은 단 하나의 반복문을 탈출시키도록하기떄문에
    #이중반복문안에 있는 break는 그안의 하나의 반복문만 빠져나오게 됨
    
    turn_time=0
print(count)