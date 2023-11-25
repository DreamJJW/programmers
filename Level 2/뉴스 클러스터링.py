def solution(str1, str2):
    cnt = 0
    union = []
    union2 = []
    temp = []
    new_str1 = ''
    new_str2 = ''
    for i in str1:
        if i.isalpha():
            new_str1 += i
    for i in str2:
        if i.isalpha():
            new_str2 += i

    for j in range(len(new_str1)-1):
        union.append(new_str1[j:j+2])

    for j in range(len(new_str2)-1):
        union2.append(new_str2[j:j+2])

    print(union)
    print(union2)
    # 합집합

    # 교집합


    print(temp)
    answer = round(cnt / len(union) * 65536)
    return answer

# solution(str1='FRANCE', str2='french')
# solution(str1='aa1+aa2', str2='AAAA12')
solution(str1='handshake', str2='shake hands')