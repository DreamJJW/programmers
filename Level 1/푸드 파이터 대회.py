def solution(food):
    menu = ''
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            # 음식이 홀수면 버려진다
            food[i] -= 1
        menu += str(i) * (food[i] // 2)
    menu += '0' + ("".join(reversed(menu)))
    print(menu)

solution(food = [1, 3, 4, 6])
# solution(food = [1, 7, 1, 2])

# "".join(reversed(문자열)  = 문자열 뒤집기

# 한 선수는 왼쪽부터 오른쪽
# 다른 선수는 오른쪽부터 왼쪽
# 칼로리 순서대로 sort
# 물은 0번, 항상 1개

# 2 <= len(food) <= 9
# 음식의 배치를 return

# [1, 3, 4, 6]
# 0이 1개, 1이 3개, 2가 4개, 3이 6개
# 0111222333333 -> 1223330333221
# 3332210122333
