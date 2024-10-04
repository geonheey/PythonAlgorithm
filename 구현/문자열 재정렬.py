# # 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력
# # 모든 알파벳을 오름차순으로 정렬하여 이어서 출력하고, 그 뒤에 모든 숫자를 더한 값 이어서 출력

input_data = input()
# 424RFD
# ['4', '2', '4', 'R', 'F', 'D']
array=[]
total = 0
# for i in range(len(input_data)):
#     if(input_data[i].isalpha()) :
#         array.append(input_data[i])
#     else :
#         total += int(input_data[i])
# array.sort()
# print(''.join(array) + str(total))  # 리스트를 문자열로 변환 후, 숫자의 합을 이어서 출력

for x in input_data :
    if x.isalpha() :
        array.append(x)
    else:
        total += int(x)

array.sort()

if(total!=0):
    array.append(str(total))

print(''.join(array))