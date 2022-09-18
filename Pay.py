##Write a pay computation code to give the employee their weekly pay rate.
##Include overtime pay(1.5x) if worked over 40 hours.

h = float(input("How many hours did you work this week?"))
r = float(input("What is your hourly rate?"))
otr = 1.5
# hours = 45
# rate = 10

if h>40:
    n = (h-40)
    print("Your weekly pay is", 40*r + n*r*otr)
else:
    print("Your weekly pay is", h*r)