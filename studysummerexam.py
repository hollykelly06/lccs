# (ii) Functions for addition and subtraction
def add(x, y):
	return x + y
def subtract(x, y):
	return x - y
# (i) Function for division, rounding to one decimal place
def divide(x, y):
	return round(x / y, 1)
# (iii) Function to perform multiple calculations
def perform_calculations(num_calculations):
	for i in range(1, num_calculations + 1):
		print(f"Calculation {i}:")
		choice = input("Select operation:\n1. Multiply\n2. Divide\n3. Add\n4. Subtract\nEnter choice(1/2/3/4): ")
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		if choice == '1':
			print(f"{num1} * {num2} = {multiply(num1, num2)}")
		elif choice == '2':
			print(f"{num1} / {num2} = {divide(num1, num2)}")
		elif choice == '3':
			print(f"{num1} + {num2} = {add(num1, num2)}")
		elif choice == '4':
			print(f"{num1} - {num2} = {subtract(num1, num2)}")
# Main Program
import random
print("Select operation.")
print("1. Multiply")
print("2. Divide")
print("3. Add")
print("4. Subtract")
choice = input("Enter choice(1/2/3/4): ")
# (iii) Allow the user to specify the number of calculations
num_calculations = int(input("How many calculations do you want to perform? "))
# Check for valid choices and perform calculations
if choice in ['1', '2', '3', '4']:
	if choice == '1' or choice == '2':
		perform_calculations(num_calculations)
	elif choice == '3' or choice == '4':
		perform_calculations(num_calculations)
else:
	print("Invalid choice.")

