import random
    number = random.randint(1,10)
    while True:
        guess = int(input("Guess the number between 1 and 10  "))
        if guess == number:
            print("You guessed the number right. ")
            break
        elif guess > number:
            print("Your guess is too high. Try again  ")
        else:
            print("Your guess is too little. Try again  ")
