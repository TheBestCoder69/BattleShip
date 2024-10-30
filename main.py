import numpy as np

def battleShip():
    # Varibles
    hit = False
    shots = 0

    x, y = map(int, input("Type in the X and Y you want to give the board").split())

    # Creates a 2d array called "Board"
    board = np.array([[0] * x] * y, dtype=str)

    # Randomly sets the Ships X and Y 
    shipX = np.random.randint(0, x)
    shipY = np.random.randint(0, y)

    # Places the Ship at the random X and Y 
    board[shipX, shipY] = 1

    while hit == False:

        # Asks the User where they should deploy the Bomb
        userX, userY = map(int, input("Type in the X and Y you want to lauch the Bomb: ").split())

        shots += 1

        print(board)

        if board[userX, userY] == "1":
            print("HIT")
            hit = True
        else:
            print("MISS")
            board[userX, userY] = "X"
            print(board)



battleShip()








