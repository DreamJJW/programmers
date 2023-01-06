def solution(my_string):
    answer = []
    for num in my_string:
        if num.isdigit():
            answer.append(int(num))
    answer.sort()
    print(answer)
    return answer

solution(my_string='p2o4i8gj2')