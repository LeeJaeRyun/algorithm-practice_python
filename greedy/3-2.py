#N M K 가 주어짐
#N=배열원소개수
#배열이 있을때 배열의 원소들을 활용해 M번 더하여 가장 큰수를 만듦
#한 수를 연속해서 K번 초과해서 더할 수 없음
#다른인덱스의 같은 숫자는 다른걸로 인식
n,m,k = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
arr.sort(reverse=True)

while True:
  for i in range(k):
    if m==0:
      break
    result+=arr[0]
    m-=1
  if m==0:
    break
  result+=arr[1]
  m-=1
print(result)