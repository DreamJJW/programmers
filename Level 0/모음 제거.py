def solution(my_string):
    for i in "".join(my_string):
        if i not in 'aeiou':
            print(my_string)


solution(my_string='nice to meet you')