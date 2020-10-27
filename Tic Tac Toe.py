# loop begins before init is run
runagain = True

# initialize new game
def init():
    # Reset Global Variables
    global indexes
    global playerturn
    global playerchoice
    global noWinner 

    indexes = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # will be used to track sections
    playerturn = 1  # default to first player's turn
    playerchoice = {'1': '', '2': ''}  # dictionary that holds XO choice
    noWinner = True
    display_board()
    choice = XO()
    assignval(choice)
## Define Functions
# Display Board Function
def display_board():
    gameboard = updateboard(indexes) # updates/redefines gameboard before displaying 
    print(gameboard)
# Player 1 Choose X or O using input / while to validate
def XO():
    choice = 'wrong'
    accvalues = ['X', 'O']
    while choice.upper() not in accvalues:
        choice = input('Player 1, would you like to be Xs or Os? (X, O): ') 
        if choice.upper() not in accvalues:
            print('This is not an acceptable choice. Please choose X or O.')
    return choice.upper()
# Assign Values to players
def assignval(choice):  # based on XO function, assign players teams using playerchoice dict
    playerchoice['1'] = choice
    if choice == 'X':
        playerchoice['2'] = 'O'
    elif choice == 'O':
        playerchoice['2'] = 'X'

# Player 1 Turn - choose position and update list
def turn():
    accvalues = list(range(1, 10))  #locally defines acceptable values
    openvalues = []
    for a, b in list(enumerate(indexes)):  # generates a list of open values
        if b == ' ':
            openvalues.append(a + 1)
        else:
            pass
    choice = 'wrong'  # blatantly wrong as to not slip through validation test
    while choice not in openvalues:  
        try:
            choice = int(input('Pick an open position between 1 and 9: '))  # if the value can't be an integer, not acceptable
        except ValueError:
                pass
        if choice not in openvalues:  # if an int, here's why it was wrong
            if choice in accvalues:
                print('This spot has already been chosen.')
            elif choice not in accvalues:
                print('That is not an acceptable value.')

    if playerturn == 1:  # determines whether to put X or O
        indexes[choice - 1] = playerchoice['1']
    elif playerturn == 2:
        indexes[choice - 1 ] = playerchoice['2']
    display_board()  # simultaneously update and display gameboard
     

    # update gameboard with new indexes
def updateboard(indexes):
    gameboard = (f'\n{indexes[0]}|{indexes[1]}|{indexes[2]}\n-----'  
    f'\n{indexes[3]}|{indexes[4]}|{indexes[5]}\n-----'
    f'\n{indexes[6]}|{indexes[7]}|{indexes[8]}')  # function updates gameboard locally 
    return gameboard                              # must assign gameboard = update(indexes)
                                                  # this is done in the displayboard function
# changes playerturn
def changeturn():
    global playerturn
    if playerturn == 1:
        playerturn = 2
    elif playerturn == 2:
        playerturn = 1
# Check for 3 in a row
def check3(indexes):
    if indexes[4] != ' ':  # check for touching 5
        if indexes[4] == indexes[6] == indexes[2]:  # check for diagonals
            return True
        elif indexes[4] == indexes[0] == indexes[8]:
            return True

        elif indexes[4] == indexes[1] == indexes[7]: # check for horizontal and vertical middle
            return True
        elif indexes[4] == indexes[3] == indexes[6]:
            return True

    if indexes[6] != ' ': #check for touching 7
        if indexes[6] == indexes[7] == indexes[8]:
            return True
        elif indexes[6] == indexes[3] == indexes[0]:
            return True

    if indexes[2] != ' ': #check for touching 3
        if indexes[2] == indexes[1] == indexes[0]:
            return True
        elif indexes[2] == indexes[5] == indexes[8]:
            return True

# Check for Cat's game
def catsgame(indexes):
    if ' ' not in indexes:
        return True
    else:
        return False
# Play Again?
def playagain():
    pick = 'wrong'
    accvalues = ['Y', 'N']
    while pick.upper() not in accvalues:
        pick = input('Would you like to play again? [Y/N]: ')
    if pick.upper() not in accvalues:
        print('That is not an acceptable value.')
    return pick.upper()

## Body Code
while runagain == True: # determines whether or not to run the program again
    init()
    while noWinner == True:
        print(f"Player {playerturn}'s turn. ({playerchoice[f'{playerturn}']}s)")
        turn()
        if check3(indexes) == True:
            print(f'Congratulations Player {playerturn}! You are the winner!')
            noWinner = False
        if catsgame(indexes) == True:
            print("Cat's game! This match ends in a draw...")
            noWinner = False
        changeturn()
    if playagain() == 'Y':
        pass
    else:
        print('Thanks for playing!')
        runagain = False
