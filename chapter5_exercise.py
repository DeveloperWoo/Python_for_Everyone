'''
Exercise 5.2:
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
'''
print("<Exercise 5.2>")

largest = None
smallest = None
while True:
    numInStr = input("Enter a number: ")
    if numInStr == "done" : break
    try:
        numInNum = int(numInStr)
        #largest number
        if(largest is None):
            largest = numInNum
        if(numInNum > largest):
            largest = numInNum
        #smallest number
        if(smallest is None):
            smallest = numInNum
        if(numInNum < smallest):
            smallest = numInNum
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
