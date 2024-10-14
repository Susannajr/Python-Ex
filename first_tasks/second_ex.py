 while True:
        choice = int(input("Choose 1 to continue and 2 to stop  "))
        if choice == 1:
            num = int(input("Please enter any integer:  "))
            if num % 2 == 0:
                print("Your num is even  ")
            elif num % 2 == 1:
                print("Your num is odd  ")
            else:
                print("Unavailable number  ")
        else:
            print("Bye")
            break
