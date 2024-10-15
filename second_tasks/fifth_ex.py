num = int(input("Please enter any integer  "))
sum = 0
while num > 0:
    digit = int(num % 10)
    num = num/10
    sum += digit
print(f"The sum of your integers is: {sum} ")
