print("Hello, Anmol")
print("python is workinng")
a=10
b=20
c=a+b
print("the sum of a and b is",c)
d=a-b
print("the difference of a and b is",d)
e=a*b
print(" the multiplication of a and b is",e)
f=a/b
print("the division of a and b is",f)
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
number = int(input("enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even.")
else:
    print(f"{number} is an odd.")
   number1 = int(input("enter first number;"))
number2 = int(input("enter second number;"))
hcf = 1
for i in range(1, min(number1, number2) + 1):
    if number1 % i == 0 and number2 % i == 0:
        hcf = i
        print(f"the hcf of {number 1} and {number 2} is {hcf}"end="")")
