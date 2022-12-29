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