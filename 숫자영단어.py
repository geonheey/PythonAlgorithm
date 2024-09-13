def solution(s, n):
    tmp = ""
    arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in s:
        if i == " ":
            tmp += " "
        elif i.islower():
            num = arr.index(i) + 1
            tmp += arr[num%26]
        elif i.isupper():
            num = arr.index(i) +1
            tmp += arr[num%26]

    return tmp
print(solution("a z",2))
