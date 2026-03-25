print("Simple Calculator")
a= float(input("Enter first number: "))
b= float(input("Enter second number: "))
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")  
print("4. Division")
choice = input("Enter choice (1/2/3/4): ")
if choice == '1':
    print(a, "+", b, "=", a+b)
elif choice == '2':
    print(a, "-", b, "=", a-b)
elif choice == '3':
    print(a, "*", b, "=", a*b)
elif choice == '4':  
    print(a, "/", b, "=", a/b)
else:
    print("Invalid input")