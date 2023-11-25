def solution(keymap, targets):
    key_map = {}
    answer = []
    for key in keymap:
        for i, j in enumerate(key):
            if j in key_map:
                if key_map[j] > i + 1:
                    key_map[j] = i + 1
            else:
                key_map[j] = i + 1
        print(key_map)


    for i in targets:
        cnt = 0
        for j in i:
            if j in key_map:
                cnt += key_map[j]
            else:
                return -1
        answer.append(cnt)

    print(answer)
    return answer



solution(keymap=["ABACD", "BCEFD"], targets=["ABCD", "AABB"])