from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(list(queue)) #list로 형변환해주면 deque자료형은 list로 깔끔하게 변환할 수 있음
