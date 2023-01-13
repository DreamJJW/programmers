def solution(s):
    res = ''
    answer = list(s.split(' '))
    for i in answer:
        for j in range(len(i)):
            if j % 2 == 0:
                res += i[j].upper()
            else:
                res += i[j].lower()
        res += " "
    return res[0:-1]
    print(res)

solution(s = "  try  hello  world  ")

# 문자열의 처음이나 끝이 공백일 수도 있다.
# split()와 split(' ')의 차이를 알아두자.
# split()은 공백이 하나든 여러개든 무조건 1개로 처리. split(" ")은 아니다.

