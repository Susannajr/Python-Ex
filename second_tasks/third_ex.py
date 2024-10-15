n = int(input("Please input the number of terms that you want to calculate the Fibonaccies sequence  "))
a = int(input("Please enter the first integer  "))
b = int(input("Please enter the second integer  "))
sum = 0
for i in range (1, n):
    sum = a + b
    a, b = b, sum
    print(f"Your total is: {sum}")
