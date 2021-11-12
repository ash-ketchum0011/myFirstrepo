board = [' ' for x in range(9)]#Board creation

def insertletter(letter,pos): #Insert letter on the board at the position input
    board[pos]= letter
    
def spaceIsfree(pos):         #Checks if space is free at the input
    return board[pos]==' '
    
def printBoard(board):        #Printing board
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('_______________________')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('_______________________')
    print(f' {board[6]} | {board[7]} | {board[8]}')
    
def isBoardFull(board):      #checks if board is full or not
    if board.count(' ')>1:
        return False
    else:
        return True
    
def isWinner(board,letter):  #checks if the letter entered is winner
    return ((board[0]==letter and board[1]==letter and board[2]==letter) or 
    (board[3]==letter and board[4]==letter and board[5]==letter) or 
    (board[6]==letter and board[7]==letter and board[8]==letter) or
    (board[0]==letter and board[3]==letter and board[6]==letter) or
    (board[1]==letter and board[4]==letter and board[7]==letter) or
    (board[2]==letter and board[5]==letter and board[8]==letter) or
    (board[0]==letter and board[4]==letter and board[8]==letter) or
    (board[2]==letter and board[4]==letter and board[6]==letter))

def playerMove():           #checks whether input is correct or not and then place the letter
    run = True
    while run:
        move= input('Please select a position to the x between 0 to 8: ')
        try:
            move= int(move)
            if move >= 0 and move < 9:
               if spaceIsfree(move):
                    run = False #If the input is correct then loop ends
                    insertletter('X', move)
               else:
                   print('Sorry, This position is occupied')
            else:
                print('Please enter a correct input')
                
        except:
            print('Please enter a number!!')
            
def computerMove():     
    possibleMoves = [x for x,letter in enumerate(board) if letter ==' '] #creates a list of indexes where letter is equal to ' '
    move=0
    for let in ['O','X']:
        for i in possibleMoves:
            boardcopy= board[:]
            boardcopy[i]=let
            if isWinner(boardcopy,let):
                move= i 
                return move
    cornersOpen= []
    for i in possibleMoves:
        if i in [0,2,6,8]:
            cornersOpen.append(i)
    if len(cornersOpen)>0:
        move = selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move=5
        return move
    edgesOpen =[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append[i]
    if len(edgesOpen)>0:
        move= selectRandom(edgesOpen)
        return move
            
def selectRandom(liSt):
    import random 
    ln = len(liSt)
    r= random.randrange(0,ln)
    return liSt[r]
    
def main():
    print('Welcome to the game')
    printBoard(board)
    
    while not(isBoardFull(board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print('sorry you loose!')
            break
        
        if not(isWinner(board,'X')):
            move=computerMove()
            if move==0:
                print(" ")
            else:
                insertletter('O',move)
                print(f'Computer placed an O on position {move} :')
                printBoard(board)
        else:
            print('You win!')
            break
        
    if isBoardFull(board):
        print("Tie game")
        
while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
