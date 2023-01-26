def solution(answers):
    stu1 = [1,2,3,4,5] * 2000
    stu2 = [2,1,2,3,2,4,2,5] * 1250
    stu3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    cnt1 = 0; cnt2 = 0; cnt3 = 0
    score = []; answer = []

    for i in range(len(answers)):
        if answers[i] == stu1[i]:
            cnt1 += 1
    score.append(cnt1)
    for i in range(len(answers)):
        if answers[i] == stu2[i]:
            cnt2 += 1
    score.append(cnt2)
    for i in range(len(answers)):
        if answers[i] == stu3[i]:
            cnt3 += 1
    score.append(cnt3)

    a = max(score)
    for i in range(len(score)):
        if score[i] == a:
            answer.append(i + 1)
    print(answer)

solution(answers=[1,2,3,4,5])

# score = [2, 2, 2]