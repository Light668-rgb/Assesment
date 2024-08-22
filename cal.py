num_1=int( input("Enter first number: "))
operator =input("Enter operator: ")
num_2= int(input("Enter second number: "))
if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1 - num_2)
elif operator == "*":
    print(num_1 * num_2)
elif operator == "/":
    print(num_1 / num_2)
elif operator == "^":
    print(num_1 ** num_2)
elif operator == "%":
    print(num_1 % num_2)
else:
    print("Invalid operator")