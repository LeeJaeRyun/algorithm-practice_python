n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(x,y):
  #예외처리를 꼭 해줘야함. 2차시도 : 예외처리를 안함
  if x<0 or y<0 or x>=n or y>=m:
    return False
  if arr[x][y]==0:
    arr[x][y]=1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False

count=0
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      count+=1
print(count)