import sys
input = sys.stdin.readline

num = int(input()) ## 입력 받을 정수의 개수
list = list(map(int,input().split())) ## 입력 받은 정수들

# 방법 1
# min = min(list)
# max = max(list)

# 방법 2
max = list[0]
min = list[0]

for i in list[1:] : 
    if i > max :
        max = i
    if i < min :
        min = i

print(min, max)