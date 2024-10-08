# first exercise
def choice():
    sum =0
    while True:
            choice =int(input("Please choose 1 to add numbers or 2 to stop"))
            if choice == 1
                num = float(input("Please input a number"))
                sum += num
                print(f"Sum is: {sum}")
            elif choice == 2
            print(f"Final sum is: {sum}")
            break
        else:
            print("invalid choice. Please choose 1 or 2.")
            choice()

# second exercise
def number():
    while True:
        choice = int(input("Choose 1 to continue and 2 to stop"))
        if choice == 1:
            num = int(input("Please enter any integer:"))
            if num % 2 == 0:
                print("Your num is even")
            elif num % 2 == 1:
                print("Your num is odd")
            else: 
                print("Unavailable number")
        else:
            print("Bye")
            break
number()

# third exercise


def calculator():
    while True:
        choice = int(input("Choose 1 to add, 2 to subtract, 3 to divide, 4 to multiple and 5 to end"))
        num1 = int(input("Please enter the first number:"))
        num2 = int(input("Please enter the second number:"))
        if choice == 1:
            sum = num1 + num2
            print(f"Your Sum is:{sum}")
        elif choice == 2:
            sub = num1 - num2
            print(f"Your Subtraction is:{sub}")
        elif choice == 3:
            if num1 == 0 or num2 == 0:
                print("Choose real number")
            else:
                div = num1 / num2
                print(f"Your division is:{div}")
        elif choice == 4:
            mul = num1 * num2
            print(f"Your multiple is:{mul}")
        elif choice == 5:
                break
        else: 
            print("No existing choice. Please choose between existing ones")
calculator()
        
# fourth exercise
import random
def number_guess():
    number = random.randint(1,10)
    while True:
        guess = int(input("Guess the number between 1 and 10"))
        if guess == number:
            print("You guessed the number right.")
            break
        elif guess > number:
            print("Your guess is too high. Try again")
        else:
            print("Your guess is too little. Try again")
number_guess()

# fifth exercise 
def factorial(n):
    if(n==0 or n ==1):
        return 1
    else: 
        return n * factorial(n-1)
num = int(input("Please enter non negative number"))
if (num>=0)
    fac=factorial(num)
    print(f"Your factorial is:{fac}")
else:
    print("Please choose valid number")

# sixth exercise
def palindrome():
    word = str(input("Please enter a word"))
    while True:
        if (word == (word[::-1])):
            print("Your word is palindrome")
            break
        else:
            print("Unfortunately it is not palindrome :(")
            break
palindrome()

# seventh exercise 
def multiplication():

    num = int(input("Please enter a number"))
    for i in range (1, 11):
        mul = num * i
        print(f"{mul} = {num} * {i}")

multiplication()

