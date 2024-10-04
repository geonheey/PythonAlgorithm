# 왕실 정원 8X8 체스판
# 나이트는 L자 형태로만 이동 가능, 정원 밖으로 못 나감
# 나이트의 이동
# 1. 수평으로 두 칸 이동 후 수직으로 한 칸 이동
# 2. 수직으로 두 칸 이동 후 수평으로 한 칸 이동
# 문제 : 나이트 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수?
# 행 위치 : 1 ~ 8
# 열 위치 : a ~ h
# ex. c2에 있을 때 이동할 수 있는 경우의 수 = 6
# 현재 나이트 위치 입력 받기
# 나이트가 이동할 수 있는 8가지의 방향 정의
# 그 다음 위치로 이동 가능한지 확인 if 가능 then 카운트 증가

input_data = input()
row_data = int(input_data[1])
col_data = ord(input_data[0])-ord('a') + 1 #이렇게 함으로써 a : 1, b : 2, c : 3가 될 수 있음

possible_pos = [(-2,1),(-2,-1), (2,1), (2,-1), (1,2),(-1,2),(-1,-2),(1,-2)]

result = 0

for pos in possible_pos :
    new_row = row_data + pos[0]
    new_col = col_data + pos[1]
    if(new_row >=1 and new_row <=8 and new_col >=1 and new_col <=8 ):
        result +=1

print(result)