#Write a program that repeatedly prompts a user for
#integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except
#and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

smallest = None
largest = None

while True:
    line = input("Enter a value:\n")
    try:
        line = int(line)
        if smallest is None or line < smallest:
            smallest = line
        if largest is None or line > largest :
            largest = line
    except:
        if line == 'Done' or line == 'done':
            break
        else:
            print("Invalid input")
            continue
print("Maximum is",largest)
print("Minimum is", smallest)
