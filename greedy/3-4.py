n,m = map(int, input().split())

result=0
for i in range(n):
  data = list(map(int, input().split()))
  min_value=10001
  for j in data:
    min_value = min(j,min_value)
  result = max(result, min_value)
print(result)