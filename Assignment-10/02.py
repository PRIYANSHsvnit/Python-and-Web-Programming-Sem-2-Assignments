import random

def isvalid(board):
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j):
                return False
            
    return True

def generatesolution(n=8):
    while True:
        board = list(range(n))
        random.shuffle(board)
        if isvalid(board):
            return board
        
def printboard(board):
    n = len(board)

    for row in range(n):
        line = ["Q" if board[col] == row else "?" for col in range(n)]
        print(" ".join(line))

    print()

solution = generatesolution()
print("Randomly Generated Solution = ", solution)
printboard(solution)