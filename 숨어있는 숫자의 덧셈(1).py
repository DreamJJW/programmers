def solution(my_string):
    answer = 0
    for num in my_string:
        if num.isdigit():
            answer += int(num)
    return answer

solution(my_string="aAb1B2cC34oOp")