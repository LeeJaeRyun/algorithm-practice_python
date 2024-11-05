n = int(input())
datas = input().split()

x,y = 1,1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
move_types=['L','R','U','D']

for data in datas:
  for i in range(len(move_types)):
    if data == move_types[i]:
      change_x = x+dx[i]
      change_y = y+dy[i]
  if change_x>n or change_y>n or change_x<1 or change_y<1:
    continue #이동한 change_x change_y가 영역을 벗어나면 이동하지않고 다음 data로 이동
  x,y = change_x, change_y
print(x,y)