n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first_num = data[n-1]
second_num = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)* k)
count += m % (k+1)




