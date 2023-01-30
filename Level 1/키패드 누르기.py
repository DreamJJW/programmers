def solution(numbers, hand):
    answer = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}

    start_left = dic['*']
    start_right = dic['#']

    for i in numbers:
        x = dic[i]
        if i in [1, 4, 7]:
            answer += 'L'
            start_left = x
        elif i in [3, 6, 9]:
            answer += 'R'
            start_right = x
        elif i in [2, 5, 8, 0]:
            a_x = start_left[0] - x[0]
            a_y = start_left[1] - x[1]
            dis_left = abs(a_x) + abs(a_y)

            b_x = start_right[0] - x[0]
            b_y = start_right[1] - x[1]
            dis_right = abs(b_x) + abs(b_y)

            if dis_right < dis_left:
                answer += 'R'
                start_right = x
            elif dis_left < dis_right:
                answer += 'L'
                start_left = x
            elif dis_left == dis_right:
                if hand == "left":
                    answer += 'L'
                    start_left = x
                else:
                    answer += 'R'
                    start_right = x
    print(answer)
    return answer

solution(numbers = [7,0,8,2,8,3,1,5,7,6,2], hand="left")

# [1,1] [3,0]
