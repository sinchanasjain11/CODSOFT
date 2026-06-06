

print("Welcome to Simple Calculator!")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("\nEnter your choice: ")

if choice == "1":
    result = num1 + num2
    print("Answer:", result)

elif choice == "2":
    result = num1 - num2
    print("Answer:", result)

elif choice == "3":
    result = num1 * num2
    print("Answer:", result)

elif choice == "4":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        result = num1 / num2
        print("Answer:", result)

else:
    print("Invalid choice!")
