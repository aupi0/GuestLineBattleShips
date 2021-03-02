import random


class Battleships:
    #gridSize is required to be an integer
    def __init__(self, gridSize):
        self.grid = [[0] * gridSize for i in range(gridSize)]
        self.guesses = 0
        self.ships = [5, 4, 4]

    def startGame(self):
        print("Welcome to Battleships!")
        print("Grid size is " + str(len(self.grid)) + "x" + str(len(self.grid)))
        print(str(len(self.ships)) + " Random ships have been generated within the board")
        print("Ships are:")
        for i in range(0, len(self.ships)):
            print(str(self.ships[i]) + " squares long")
        self.populateGrid()
        playing = True
        while playing:
            if self.checkEmpty():
                print("Congratulations you Won the game in " + str(self.guesses) + " rounds!!")
                playing = False
            else:
                guess = self.userGuess()
                validGuess = self.validGuess(guess)
                while not validGuess:
                    print("Invalid userInput please try again")
                    guess = self.userGuess()
                    validGuess = self.validGuess(guess)
                col, row = self.convertGuess(guess)
                self.playGuess(col, row)
                self.guesses += 1

    def populateGrid(self):
        shipsPlaced = 0
        while shipsPlaced < len(self.ships):
            direction = random.randint(0,1)
            randRow = random.randint(0, len(self.grid) - 1)
            randCol = random.randint(0, len(self.grid) - 1)
            if direction == 0:
                if randCol + (self.ships[shipsPlaced] - 1) < len(self.grid):
                    validLocation = True
                    for i in range(randCol, randCol + self.ships[shipsPlaced]):
                        if (self.grid[i][randRow] != 0):
                            validLocation = False
                    if validLocation:
                        for i in range(randCol, randCol + self.ships[shipsPlaced]):
                            self.grid[i][randRow] = shipsPlaced + 1
                        shipsPlaced += 1
            if direction == 1:
                if randRow + (self.ships[shipsPlaced] - 1) < len(self.grid):
                    validLocation = True
                    for i in range(randRow, randRow + self.ships[shipsPlaced]):
                        if (self.grid[randCol][i] != 0):
                            validLocation = False
                    if validLocation:
                        for i in range(randRow, randRow + self.ships[shipsPlaced]):
                            self.grid[randCol][i] = shipsPlaced + 1
                        shipsPlaced += 1

    def checkEmpty(self):
        for col in range(0, len(self.grid)):
            for row in range(0, len(self.grid)):
                if self.grid[col][row] in range(1, len(self.ships) + 1):
                    return False
        return True
    
    def userGuess(self):
        print("Select Grid Column (A-J) and Grid Row (0-9), Example input A5")
        userInput = input("Guess: ")
        print("userInput = ", userInput)
        return userInput

    def playGuess(self, col, row):
        if self.grid[col][row] in range(1, len(self.ships) + 1):
            print("Hit!!")
            
            sunk = True
            if col != len(self.grid) - 1:
                if self.grid[col+1][row] == self.grid[col][row]:
                    sunk = False
            if col != 0:
                if self.grid[col-1][row] == self.grid[col][row]:
                    sunk = False
            if row != len(self.grid) - 1:
                if self.grid[col][row+1] == self.grid[col][row]:
                    sunk = False
            if row != 0:
                if self.grid[col][row-1] == self.grid[col][row]:
                    sunk = False

            if sunk:
                print("Ship Sunk!!")
            self.grid[col][row] = "x"
        else:
            print("Miss!!")

    def validGuess(self, userInput):
        if len(userInput) != 2:
            return False
        elif not ((ord(userInput[0].lower()) - 97) < len(self.grid) and (ord(userInput[0].lower()) - 97) >= 0):
            return False
        elif not userInput[1].isdigit():
            return False
        elif not (int(userInput[1]) < len(self.grid) and int(userInput[1]) >= 0):
            return False
        else:
            return True
    
    def convertGuess(self, userInput):
        userCol = userInput[0]
        userRow = userInput[1]
        userColInt = ord(userCol.lower()) - 97
        return userColInt, int(userRow)
    
b = Battleships(10)
b.startGame()
