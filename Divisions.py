num = int(input("Pick a number, any number!"))
num1 = int(input("Choose another number, please.)

if(num%4 == 0):
    print("Your number is divisble by 4")
elif(num%2 == 0):
    print("Your number is divisible by 2")
else:
    print("You have selected an odd number")
    
if(num%num1 == 0):
    print(num, "is evenly divided by", num1, "which equals", num/num1)
else:
    print(num, "is not evenly divided by", num1)
