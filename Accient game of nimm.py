def main():
#Total number of stones present.
    stone= 20
    player = 1
# This loop will run until there are zero stones left.
    while stone > 0:
#This statement will print the number of stones left before
#stones were picked by any player.
        print("There are "+str(stone)+" stones left")
#turn stores the infromation about which of the player has to pick now.
#function get_turn is assigned to the turn in which player acts as a variable.
        turn = get_turn(player)
#player +=1 increments every time so that players can pick stones alternatelty.
        player +=1
#compute_amount function have two variables stone and turn.
#new value to the stone assigned here.
        stone= compute_amount(stone,turn)
        print(' ')
#winner function in the end prints the player number opposite to the player who
#picked the last stone/stones.
    winner(turn)
def compute_amount(stone,turn):
    amount = int(input("Player "+str(turn)+" would you like to remove 1 or 2 stones? "))
    while amount !=1 and amount !=2:
        amount= int(input("Please enter 1 or 2: "))
    stone = stone - amount
#stone on the RHS is the variable to which 20 is assigned at the starting.
#stone on the LHS is the verified value of the stone after the amount of stones
#enter by the player subtracted from it.
    return stone
def get_turn(player):
    if player%2 ==0:
        return 2
    else:
        return 1
def winner(turn):
    if turn==2:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
if __name__ == '__main__':
    main()
