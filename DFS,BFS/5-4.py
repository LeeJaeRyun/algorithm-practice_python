def recursive_function(i):
  if i==100:
    return
  print(i,'번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
  recursive_function(i+1)
  print(i,'번째 재귀 함수를 종료합니다.')
recursive_function(1)

#컴퓨터 내부에서 재귀함수의 수행은 스택 자료구조를 이용함
#함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료 되기 때문