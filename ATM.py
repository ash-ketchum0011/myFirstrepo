def checkpin(Pin):
    if Pin == password:
        return True
    else:
        return False
def balance_processing():
    global balance
    amount= abs(int(input("Please enter amount to withdraw: ")))
    while amount>balance:
        print("Entered amount exceeds the limit")
        amount= abs(int(input("Please enter amount to withdraw: ")))
    balance-= amount
    print(f"{amount} INR is withdrawl.")
    print(f"Available balance {balance}")
def processing(enter):
    if enter==1:
        balance_processing()
    elif enter==2:
        print(f"Available balance in your account {balance}")
def next_process():
    print("For cash withdrawl enter: 1")
    print("For balance check enter: 2")
    enter= int(input("Enter: "))
    while enter!=1 and enter!= 2:
        print("Please enter valid number")
        enter= input("Enter: ")
    if enter==1:
        processing(enter)
    elif enter==2:
        processing(enter)

Pin =int(input("Please enter your Pin: "))
balance=1000
Chances =3
password= 7777
while checkpin(Pin)==False:
    if Chances>0:
        Chances-=1
        print("Enter Valid Pin")
        Pin =input("Please enter your Pin: ")
        checkpin(Pin)
    else:
        break
if Chances==0:
    print("Pin you are trying to provide is wrong, Try again later")
else:
    next_process()
