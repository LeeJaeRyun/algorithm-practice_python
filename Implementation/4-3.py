input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1
#ord함수로 반환한 자료의 자료형은 정수형값이기 때문에 int()로 굳이 안해줘도 됨

steps = [(-2,-1), (-2,1), (2,1), (2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
result = 0

for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]
  if next_row >=1 and next_row <=8 and next_column >=1 and next_column<=8:
    result+=1
print(result)

