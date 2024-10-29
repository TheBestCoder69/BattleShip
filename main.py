import numpy as np

# Sets up board
board = np.array([[0] * 5] * 5)

# Gets random X and Y for the ship
shipX = np.random.randint(0, 5)
shipY = np.random.randint(0, 5)

# Places ship in a random area in the "ocean"
board[shipX, shipY] = 1

#User input for target location
x = int(input("x point of target"))
y = int(input("y point of target"))

def tableSetup():
    print(board)

tableSetup()

if (board[x,y]==1):
    print("HIT")
else:
    print("Miss")
