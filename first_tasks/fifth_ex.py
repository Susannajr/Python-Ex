def factorial(n):
    if(n==0 or n ==1):
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Please enter non negative number  "))
if (num>=0)
    fac=factorial(num)
    print(f"Your factorial is:  {fac}")
else:
    print("Please choose valid number  ")
