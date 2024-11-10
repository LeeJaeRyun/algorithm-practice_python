stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])
#[start:stop:step]
#step:슬라이싱간격정함. 양수면 오른쪽으로 음수면 왼쪽으로 이동