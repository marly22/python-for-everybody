# #Rewrite your pay computation with time-and-a-half for
# overtime and create a function called computepay which takes two parameters
# (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0


try:
    hours = float(input("Enter hours:\n"))
    rate = float(input("Enter rate:\n"))
except:
    print("Enter a numerical value")

def computepay(hours,rate):
    if hours <= 40:
        return hours * rate
    else:
        return (40*10)+(hours-40)*1.5*10


x = computepay(hours,rate)
print("Pay:", x)
