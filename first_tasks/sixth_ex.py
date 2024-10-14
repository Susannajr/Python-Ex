word = str(input("Please enter a word  "))
    while True:
        if (word == (word[::-1])):
            print("Your word is palindrome  ")
            break
        else:
            print("Unfortunately it is not palindrome: ")
            break
