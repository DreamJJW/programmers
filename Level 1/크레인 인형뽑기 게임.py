def solution(board, moves):
    box = []; cnt = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                box.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(box) > 1 and box[-1] == box[-2]:
            box.pop(-1)
            box.pop(-1)
            cnt += 2
    print(box)
    print(cnt)

solution(board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], moves= [1,5,3,5,1,2,1,4])



# [[0,0,0,0,0],
#  [0,0,1,0,3],
#  [0,2,5,0,1],
#  [4,2,4,4,2],
#  [3,5,1,3,1]

# [[0,0,0,0,0],
#  [0,0,0,0,0],
#  [0,0,5,0,0],
#  [0,2,4,0,2],
#  [0,5,1,3,1]

#  moves= [1,5,3,1,5,1,2,1,4]

# 담는 순서는 = [4, 3, 1, 1, 3, 2, 4]
# 터져 사라진 인형 개수를 return

# 배운 것 pop(x)에서 x는 인덱스값이다