n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 오름차순으로 정렬

# 가장 큰 수와 두 번째로 큰 수만 저장하면 됨
# 어차피 K번 만큼만 반복하여 더 할 수 있기때문에 가장 큰 수를 K번 반복하여 더하고, 그 다음으로 
# 큰 수를 한 번 더 해주면 됨
first_num = data[n-1]
second_num = data[n-2]

result = 0
while True  :
    for i in range(k) :
        if m == 0 :
            break
        result += first_num
        m -= 1
    if m == 0 :
        break
    result += second_num
    m -= 1
    
print(result)