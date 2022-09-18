def computepay(h, r):
    if h>40:
        n = (h-40)
        print("Your weekly pay is", 40*r + n*r*otr)
    else:
        print("Your weekly pay is", h*r)

h = float(input("How many hours did you work this week?"))
r = float(input("What is your hourly rate?"))
otr = 1.5
# hours = 45
# rate = 10

computepay(h, r)