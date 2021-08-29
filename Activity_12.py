#First we have to get three numbers from user
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))
#Using 'if' condition to see the greatest number
if(num1>num2) and (num1>num3):
    print(num1,"Is the greatest among two numbers")
elif(num2>num1) and (num2>num3):
        print(num2,"Is the greatest among two numbers")
elif(num3>num1) and (num3>num2):
            print(num3,"Is the greatest among two numbers")
      
