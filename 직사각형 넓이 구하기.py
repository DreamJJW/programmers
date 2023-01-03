dots = [[0, 1], [1, 1], [1, 0], [0, 0]]
dots.sort()
height = abs(dots[3][1] - dots[2][1])
width = abs(dots[3][0] - dots[2][0])

print(dots)
print(height * width)
