from string import ascii_lowercase
def solution(s, skip, index):
    temp = ''; lst = []
    alp = list(ascii_lowercase) * 3
    for i in alp:
        if i not in list(skip):
            lst.append(i)

    for i, j in enumerate(s):
        if j in lst:
            idx = lst.index(j)
            temp += lst[idx + index]

    print(temp)


# solution(s="aukks", skip="wbqd", index=5)
solution(s="z", skip="abcdefghij", index=20)
