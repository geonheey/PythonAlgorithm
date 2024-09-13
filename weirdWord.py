def solution(s):
    tmp = ""
    answer = s.split()  
    
    for word in answer:
        for index, char in enumerate(word): 
            if index % 2 == 0: 
                tmp += char.upper()
            else :
                tmp += char.lower()
        tmp += " "
    return tmp[0:-1]


print(solution("disappeared aPpEaReD     "),"dd")  
