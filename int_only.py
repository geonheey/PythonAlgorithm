def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        return False
    if s.isdigit() :
        return answer
    else :
        return False
    
    

print(solution("123aa3"))