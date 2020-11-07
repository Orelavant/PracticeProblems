import sys

def knightPos(file):
    knightDict = {}

    for i in range(5):
        line = file.readline()
        for j in range(len(line)):
            if line[j] == "k":
                knightDict[(i, j)] = (i, j)

    return knightDict

# For every knight, check possible collisions
def knightColl(file):
    board = knightPos(file)
    if len(board.values()) != 9:
        print("invalid")
        return

    for knight in board.values():
        if checkColl(knight, board):
            return

    print("valid")

def checkColl(knight, board):
    # Find possible positions and check if any exist in board
    possibleMoves = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
    for move in possibleMoves:
        possKnight = (knight[0]+move[0], knight[1]+move[1])
        if possKnight in board:
            print("invalid")
            return True
    return False

file = sys.stdin
knightColl(file)
