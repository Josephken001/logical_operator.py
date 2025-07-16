# A simple calculator app
print("Welcome to my Super calculator")
print("""**********************
1. Addition
2. Subtraction 
3. Multiplication
4. Division
******************************""")
print("Enter two numbers to add")
# Prompts the user for a number 
first_number = input("First Number:")
# Prompts the user for  a number 
second_number = input("Second Number:")
sum = float(first_number) + float(second_number)
print (f"{first_number} + {second_number} = {sum}")

print("*******************")
print("Subtraction")
print("Enter two numbers to Subtract")
# Prompts the user for a number
first_number = input("First Number:")
# Prompts the user for  a number
second_number = input("Second Number:")
sub = float(first_number) - float(second_number)
print (f"{first_number} - {second_number} = {sub}")

print("*******************")
print("Multipliccation")
print("Enter two numbers to Multiply")
# Prompts the user for a number
first_number = input("First Number:")
# Prompts the user for  a number
second_number = input("Second Number:")
mul = float(first_number) * float(second_number)
print (f"{first_number} * {second_number} = {mul}")

print("*******************")
print("Division")
print("Enter two numbers to Divide")
# Prompts the user for a number
first_number = input("First Number:")
# Prompts the user for  a number
second_number = input("Second Number:")
div = float(first_number) / float(second_number)
print (f"{first_number} / {second_number} = {div}")

print("*******************")
print("Exponential")
print("Enter two numbers to Exponent")
# Prompts the user for a number
first_number = input("First Number:")
# Prompts the user for  a number
second_number = input("Second Number:")
expo = float(first_number) ** float(second_number)
print (f"{first_number} ** {second_number} = {expo}")
