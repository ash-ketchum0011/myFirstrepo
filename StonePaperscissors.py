def comp_turn(comp):
    list = ["stone", "paper", "scissor"]
    return list[comp]
def decision_processing(user,comp1):
    if user == comp1:
        print("It's a Tie both entered {0}".format(user))
    elif user == 'stone':
        if comp1 == 'paper':
            print("Computer wins: {0} and You loose: {1}".format(comp1,user))
        elif comp1 == 'scissor':
            print("You won: {0} and Computer loose: {1}".format(user,comp1))
    elif user == 'paper':
        if comp1 == 'scissor':
            print("Computer wins: {0} and You loose: {1}".format(comp1,user))
        elif comp1 == 'stone':
            print("You won: {0} and Computer loose: {1}".format(user,comp1))
    elif user == 'scissor':
        if comp1 == 'stone':
            print("Computer wins: {0} and You loose: {1}".format(comp1,user))
        elif comp1 == 'paper':
            print("You won: {0} and Computer loose: {1}".format(user,comp1))
import random
comp= random.randint(0,2)
user= input("Please enter your move: ")
while user != 'stone' and user !='scissor' and user !='paper':
    print('Please enter valid input')
    user= input("Please enter your move: ")
while user != '1':
    comp1 = comp_turn(comp)
    decision_processing(user,comp1)
    comp= random.randint(0,2)
    user= input("Please enter your move: ")
    while user != 'stone' and user !='scissor' and user !='paper':
        print('Please enter valid input')
        user= input("Please enter your move: ")