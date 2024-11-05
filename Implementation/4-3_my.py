locate = input()

x_step = [-2, -2, 2, 2, 1, 1, -1, -1]
y_step = [1, -1, 1, -1, 2, -2, 2, -2]
count=0

for i in range(8):
  dx = ord(locate[0])-ord('a')+1+x_step[i]
  dy = int(locate[1])+y_step[i]
  if dx<1 or dy<1 or dx>8 or dy>8:
    continue
  count+=1
print(count)
#ord함수 => 문자열을 유니코드값으로 바꿔주는 함수