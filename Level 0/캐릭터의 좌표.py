def solution(keyinput, board):
    startX = 0; startY = 0

    for i in range(len(keyinput)):
        if keyinput[i] == 'left':
            startX -= 1;
            if abs(startX) > (board[0] - 1) // 2:
                startX += 1
        elif keyinput[i] == 'right':
            startX += 1;
            if startX > (board[0] - 1) // 2:
                startX -= 1
        elif keyinput[i] == 'up':
            startY += 1
            if startY > (board[1] - 1) // 2:
                startY -= 1
        elif keyinput[i] == 'down':
            startY -= 1
            if abs(startY) > (board[1] - 1) // 2:
                startY += 1
    return startX, startY
# left right up right right
# down down down down down
