n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

#dfs로 배열을 첫번째부터 확인
#첫번째칸이 0이고 상하좌우에 0이 있다면 
#1로 바꾸고 그칸에 가서 또 상하좌우에 0이있는지 확인
#반복이 다끝나면 count+=1
#두번째칸으로가서 0이면 똑같이 수행 아니면 넘어가

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
#주어진 범위를 벗어나는 경우 종료
#현재 노드를 아직 방문하지 않았다면
#해당 노드 방문 처리
#상,하,좌,우의 위치도 모두 재귀적으로 호출
def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  if arr[x][y]==0:
    arr[x][y]=1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False

count=0
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      count+=1
print(count)