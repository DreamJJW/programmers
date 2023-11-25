def solution(cards1, cards2, goal):
    temp = []; temp2 = []

    if len(cards1) + len(cards2) != len(goal):
        return "No"

    for i, j in enumerate(cards1):
        if j in goal:
            temp.append(goal.index(j))

    for i, j in enumerate(cards2):
        if j in goal:
            temp2.append(goal.index(j))

    a = sorted(temp); b = sorted(temp2)

    if a == temp and b == temp2:
        return "Yes"
    else:
        return "No"


solution(cards1=["i", "drink", "water"], cards2=["want", "to"],
          goal=["i", "want", "to", "drink", "water"])

solution(cards1=["i", "water", "drink"], cards2=["want", "to"],
         goal=["i", "want", "to", "drink", "water"])

# 25번 테스트 케이스
# solution(cards1=["i", "drink"], cards2=["want", "to"], goal=["i", "want", "to", "drink", "water"])