import re

def solution(new_id):
    answer = ""
    final_answer = ""
    # 1단계: 소문자 변환
    new_id = new_id.lower()
    print(answer)
    # 2단계: 알파벳, 숫자, -, _, . 제외한 문자 제거
    for char in new_id:
        if char.isalnum() or char in ["-", "_", "."]:
            answer += char
    # 3단계: .이 2번 이상 연속된 부분을 .으로 치환
    answer = re.sub(r'\.{2,}', '.', answer)

    # 4단계: .으로 시작하거나 끝나는 경우 제거
    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:-1]
        
    # 5단계: 공백을 a로 치환하고, 최대 15자로 자르기
    if answer:
        answer
    else:
        answer = 'a'
    
    answer = answer.replace(" ", "a")[:15]
    
    # 6단계: .으로 끝나는 경우 제거
    if answer.endswith('.'):
        answer = answer[:-1]
    final_answer = answer
    # 7단계: 길이가 2보다 작으면 마지막 문자를 반복하여 길이를 3으로 맞춤
    while len(final_answer) < 3:
        if final_answer:  # answer가 비어있지 않은 경우에만 마지막 문자 추가
            final_answer += final_answer[-1]
        
    return final_answer

# 테스트
print(solution("=.="))
