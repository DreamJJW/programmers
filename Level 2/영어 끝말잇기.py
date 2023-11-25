def solution(n, words):
    spoken = []
    cnt = 0
    order = 1
    answer = [0, 0]
    for i in words:
        if spoken:
            if i in spoken or i[0] != spoken[-1][-1]:
                answer[1] = order
                answer[0] = cnt+1
                break
            else:
                spoken.append(i)
                cnt += 1
        else:
            spoken.append(i)
            cnt += 1

        if cnt == n:
            cnt = 0
            order += 1

    return answer

solution(n=5, words=["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure",
                     "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])

solution(n=3, words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])

solution(n=2, words=["hello", "one", "even", "never", "now", "world", "draw"])