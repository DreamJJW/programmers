board = [[0, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0]]
# 상하 좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 대각
bx = [1, 1, -1, -1]
by = [1, -1, 1, -1]

cnt = 0; n = len(board)
m= [[9] * (len(board) + 2) for _ in range(len(board) + 2)]
for x in range(n):
    for y in range(n):
        if x < n + 2 and y < n + 2:
            m[x+1][y+1] = board[x][y]

for i in range(len(m)):
    for j in range(len(m)):
        if m[i][j] == 1:
            for k in range(4):
                if m[i + dx[k]][j + dy[k]] != 1:
                    m[i + dx[k]][j + dy[k]] = 2
                if m[i + bx[k]][j + by[k]] != 1:
                    m[i + bx[k]][j + by[k]] = 2
print(m)

for i in range(len(m)):
    for j in range(len(m)):
        if m[i][j] == 0:
            cnt +=1

print(cnt)


# 지뢰는 1, 안전 지대 0
# [[0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 1, 1, 0],
#  [0, 0, 0, 0, 0]]   result = 16

# [[0, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0]]
# Test Case no.1 , res = 2