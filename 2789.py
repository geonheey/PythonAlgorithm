# 순열 조합 라이브러리 사용

# from itertools import combinations

num, total = map(int,input().split()) 
list = list(map(int,input().split())) 
result = 0

# for i in combinations(list, 3) :
#     temp_sum = sum(i)
#     if result < temp_sum <= total :
#         result = temp_sum

# print(result)


# 순열 조합 사용 X

for i in range(num) :
    for j in range(i+1, num) :
        for k in range(j+1, num) :
            if list[i] + list[j] + list[k] <= total : 

                result = max(result, list[i] + list[j] + list[k])

print(result)
