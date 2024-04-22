num1 = int(input("enter a number"))
num2 = int(input("enter a number"))

while True:
    print("inside while loop")
    choice= input("do you want loop to countinue y/n")
    if choice in ("y" , "Y"):
        print("contining....")
        num1 = int(input("enter a number"))
        num2 = int(input("enter a number"))
    else:
        break
    
    