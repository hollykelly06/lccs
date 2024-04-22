firstname = input("What is your name? ")
#user enters first name 
Surname  = input("What is your surname? ")
print("Hello ",firstname, Surname )
print("Please select from a list of items.\n")
print("\tItems Available")
print(" - - - - - - - - - ")
print("1 Book")
print("2 ruler")
print("3 pen ")
print("- - - - - - - - - ")
 


shoppingItem = int(input("\nEnter the number of items you would like: "))
if shoppingItem==1:
  print("you bought a book")
if shoppingItem==2:
  print("you bought a ruler")
if shoppingItem==3:
  print("you bought a pen")


user_input = input("Enter a number (1, 2, or 3): ")

if user_input == "1":
    print("You entered 1.")
elif user_input == "2":
    print("You entered 2.")
elif user_input == "3":
    print("You entered 3.")
else:
    print("Error: Please enter only the numbers 1, 2, or 3.")
