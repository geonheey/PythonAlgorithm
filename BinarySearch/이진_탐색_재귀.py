n, target = list(map(int, input().split()))
array = list(map(int, input().split()))


def binary_search(array, target, start, end) :
    if start > end :
        return None
    mid = (start + end)//2
    if array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] == target:
        return mid
    else :
        return binary_search(array, target, mid+1, end)
    
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else : 
    print(result + 1) # 인덱스가 반환되므로 몇 번째 원소인지 알기 위해 +1을 해준다.
    
