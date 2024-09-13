import re

def solution(new_id):
    id = new_id.lower()
    id = re.sub('[^a-z0-9\-_.]','',id)
    id = re.sub('\.{2,}','.',id)
    id = 'a' if len(id) == 0 else id[0:15]
    id = re.sub('^[.]|[.]$','',id)
    id = id if len(id) > 2 else id + "".join([id[-1] for i in range(3-len(id))])


    return id


print(solution("abcdefghijklmn.p"))