# File:    proj2.py
# Name:    Matthew Grant
# Date:    11/25/15
# Section: 03
# Email:   mgr1@umbc.edu
# Description: 
#             This program fills in the spaces in a given figure using
#             user- defined characters. 

def getFile():

    # getFile gets the name of the file which will be used in the auto-fill function
    # Input: The file name
    # Output: The file object, to be used in the function

    

    fileType = 'invalid'

    while fileType == 'invalid' :

        fileName = input("Please enter the name of a .dat or .txt file: ")

        if fileName[:-4:-1] == 'tad':

            fileType = 'data'

        elif fileName[:-4:-1] == 'txt':

            fileType = 'text'

        else:

            fileType = 'invalid'

            print("File must be a .txt or .dat file")

            
    baseFile = open(fileName, 'r')

    return baseFile



def makeList(baseFile):

    # makeList turns the raw input into a 2D list which will be edited throughout the program
    # Input: The data or text file which contains the original image
    # Output: A 2D list which the program will edit

    boardList = []

    # Turn image into a list of strings

    imageList = list(baseFile.readlines())

    for q in imageList:

        q.strip()

    boardRows = len(imageList)

    boardCols = len(imageList[0])

    for i in range(boardRows):

        boardList.append([])

        for j in range(boardCols - 1):

            boardList[i].append(imageList[i][j])

        
    
    return boardList

def printList(boardList):

    # printList prints the board
    # Input: The list comprising the board
    # Output: The board

    boardRows = len(boardList)

    boardCols = len(boardList[0])

    for x in range(boardRows):

        for y in range(boardCols):

            if (y + 1) % boardCols == 0:

                print(boardList[x][y])

            else:

                print(boardList[x][y], end = '')

            
        

               

    
def autoFill(boardList, startingRow, startingCol, printAll, fillSymbol):

    # autoFill is the function which fills the whitespace in the figure
    # Input: The board list, starting x and y, and whether the program should print each recursion, the symbol to fill the figure with
    # Output: The filled list


    if boardList[startingRow][startingCol] == ' ':

        boardList[startingRow][startingCol] = fillSymbol

        if printAll == True:

            printList(boardList)
    
    # Check surroundings (Recursive Part)

    # Base Case: All surrounding spaces are not empty
    


        if boardList[startingRow - 1][startingCol] == ' ':

            startingRow -= 1

            autoFill(boardList, startingRow, startingCol, printAll, fillSymbol)

        if boardList[startingRow][startingCol + 1] == ' ':

            startingCol += 1

            autoFill(boardList, startingRow, startingCol, printAll, fillSymbol)

        if boardList[startingRow + 1][startingCol] == ' ':

            startingRow += 1

            autoFill(boardList, startingRow, startingCol, printAll, fillSymbol)

        if boardList[startingRow][startingCol - 1] == ' ':

            startingCol -= 1

            autoFill(boardList, startingRow, startingCol, printAll, fillSymbol)

def main():

    print("Welcome to Auto-Fill!\nProgrammed by Matthew Grant")

    baseFile = getFile()
    
    boardList = makeList(baseFile)

    printList(boardList)

    userInput = 'not q'
    
    # Validate the coordinates, and run the fill function if the input isn't Q

    while userInput != 'Q':

        userInput = input("Please enter the coordinates you would like to start filling in at in the form \"row, col\", or enter Q to quit: ")

        if userInput != 'Q':

            startingRow, startingCol = userInput.split(',')

            startingRow = int(startingRow)

            startingCol = int(startingCol)

            if startingRow < 0 or startingRow >= len(boardList):

                print("Invalid input!")

                userInput = input("Try again: ")

            else:

                if startingCol < 0 or startingCol >= len(boardList[0]):

                    print("Invalid input!")

                    userInput = input("Try again: ")

            fillSymbol = input("Pick a single character to fill the figure with: ")

            while len(fillSymbol) != 1:

                fillSymbol = input("This is not a single character. Try again: ")

            printAll = input("Would you like to see every step of the recursion? Type yes or no: ")

            while printAll != 'yes' and printAll != 'no':

                printAll = input("Please enter yes or no: ")

            

            if printAll == 'yes':

                printAll = True

            else:

                printAll = False

        autoFill(boardList, startingRow, startingCol, printAll, fillSymbol)

        if userInput != 'Q':

            printList(boardList)



        

    baseFile.close()

main()
