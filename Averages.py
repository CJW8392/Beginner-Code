num = 0.0
tot = 0.0
while True:
    sval = input("Enter a number:")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    num = num + 1
    tot = tot + fval

print("You entered",num, "numbers.", "The total of that is:", tot,".", "The average of all numbers entered is:", tot/num)