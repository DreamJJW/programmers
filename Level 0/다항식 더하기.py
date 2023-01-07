polynomial = input()
x_sum = 0; num_sum = 0
polynomial = polynomial.split(' + ')
for char in polynomial:
    if 'x' in char:
        if len(char) != 1:
            x_sum += (int(char[:-1]))
        else:
            x_sum += 1
    else:
        num_sum += int(char)
        # return 0

if num_sum == 0:
    if x_sum == 1:
        print("x")
    else:
        print(str(x_sum) + "x")
elif x_sum == 0:
    print(num_sum)
else:
    if x_sum == 1:
        print("x" + " + " + str(num_sum))
    else:
        print(str(x_sum) + "x" +  " + " + str(num_sum))

# 유의 테스트 케이스
# x의 계수가 1일 때, 1x 이렇게 출력되면 오답이다.
# 식에서 변수가 없는 상수만을 return할 때, int가 아닌 str로 반환해야한다.