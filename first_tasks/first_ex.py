    sum =0
    while True:
            choice =int(input("Please choose 1 to add numbers or 2 to stop  "))
            if choice == 1:
                num = float(input("Please input a number  "))
                sum += num
                print(f"Sum is:  {sum}")
            elif choice == 2:
            print(f"Final sum is:  {sum}")
            break
        else:
            print("invalid choice. Please choose 1 or 2.  ")
