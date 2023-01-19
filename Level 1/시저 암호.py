from string import ascii_lowercase
from string import ascii_uppercase
def solution(s, n):
    answer = ''
    S_alp = "abcdefghijklmnopqrstuvwxyz" * 2
    B_alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2
    for i in range(len(s)):
        if s[i].isupper():
            answer += B_alp[B_alp.find(s[i]) + n]
        elif s[i].islower():
            answer += S_alp[S_alp.find(s[i]) + n]
        elif s[i].isspace():
            answer += ' '

    # print(answer)
    return answer

solution(s = "a B z", n = 4)