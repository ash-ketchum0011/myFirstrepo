# Hailstone sequence

def main():
    step =0
    number = int(input("Enter a number: "))
    while number>=2:
        if number%2 !=0:
            number_odd(number)
            print(number," is odd, so I make 3n + 1: ",number_odd(number))
            number = number_odd(number)
            step +=1
        elif number%2 ==0:
            number_even(number)
            print(number," is even, so I take half: ",number_even(number))
            number = number_even(number)
            step +=1
    print("The process took ",step," steps to reach 1")
def number_odd(number):
    number = int(3*number+1)
    return number
def number_even(number):
    number = int(number/2)
    return number

main()
