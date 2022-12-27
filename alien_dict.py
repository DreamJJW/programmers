from itertools import permutations
def solution(spell, dic):
    a = list(map("".join, permutations(spell)))

    for i in a:
        if i in dic:
            res = 1
            break
        else:
            res = 2
    return res