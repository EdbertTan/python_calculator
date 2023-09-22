print("input arithmetic operation\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for power")


a = input("enter number:")
while not a.isdigit():
    a = input("this is not a number. input a number")
b = int(a)
while b > 5:
    a = input("the number is too big, input number again:")
    while not a.isdigit():
        a = input("this is not a number. input a number")
    b = int(a)
    while b < 1:
        a = input("the number is too small, input number again:")
        while not a.isdigit():
            a = input("this is not a number. input a number")
        b = int(a)

x = input("enter first number : ")
while not x.isdigit():
    x = input("this is not a number. input a number")
num1 = float(x)

y = input("enter second number : ")
while not y.isdigit():
    y = input("this is not a number. input a number")
num2 = float(y)

if b == 1:
 z = num1 + num2
 print(f"result of {num1} + {num2} is {z}")
elif b == 2:
    z = num1 - num2
    print(f"result of {num1} - {num2} is {z}")
elif b == 3:
    z = num1 * num2
    print(f"result of {num1} x {num2} is {z}")
elif b == 4:
    z = num1 / num2
    print(f"result of {num1} / {num2} is {z}")
elif b == 5:
    z = num1 ** num2
    print(f"result of {num1} to the power of {num2} is {z}")