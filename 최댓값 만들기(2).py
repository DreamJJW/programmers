numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
num1 = numbers[0] * numbers[1]
num2 = numbers[-1] * numbers[-2]

if num1 > num2:
    print(num1)
else:
    print(num2)


# 1 2 -3 4 -5
# 0 -31 24 10 1 9