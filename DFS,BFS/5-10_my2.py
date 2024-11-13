n,m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
count=0

def dfs(x,y):
  if x>=n or y>=m or x<0 or y<0:
    return False
  if arr[x][y]==0:
    arr[x][y]=1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False
#3차시도(2번째 복습)
#arr[x][y]가 0이 아닌경우를고려하지 못했음
#count+=1을 할곳을 찾지 못했음
#dfs함수에서 arr[x][y]가 0인경우 True를 반환하도록하여
#메인함수에서 if문을 이용해 dfs출력이 True이면 count+=1을 하도록함

for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      count+=1
print(count)