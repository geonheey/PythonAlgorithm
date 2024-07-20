import sys
input = sys.stdin.readline

n, m = map(int, input().split()) ## n : 원본 데이터 크기, m : 질의 개수
A = [[0]*(n+1)]  ## 원본 데이터 형식
D = [[0]*(n+1) for _ in range(n+1)] ## 합 배열 저장

# A : 0으로 채워진 (n+1) 크기의 배열을 먼저 추가 -> 이로 인해 인덱스가 1부터 시작하게 되어 인덱싱이 편리해짐
# D : (n+1)x(n+1) 크기의 배열을 생성하여 모든 요소를 0으로 초기화합니다.

## 원본 데이터 생성
for i in range(n) :
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

## 합 배열 생성
for i in range(1, n+1) :
    for j in range(1, n+1) :
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

## 질의 수 받기
for _ in range(m) :
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1] ## 겹치는 부분은 더해주기
    print(result)
