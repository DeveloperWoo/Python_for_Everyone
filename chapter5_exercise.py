#A definite loop with strings
print('<A definite loop with strings>')
friends = ['Kaylee', 'Kelly', 'Iris']
for friend in friends :
    print('Happy New Year,', friend)
print('Done')
print()

#Finding the largest value
print('<Finding the largest value>')
largest_so_far = -1
print('Before loop, the largest number is', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far :
        largest_so_far = the_num
    print("Largest number:",largest_so_far, "Current number:", the_num)
print('After loop, the largest number is', largest_so_far)
print()

#Finding the smallest value
print('<Finding the smallest value>')
smallest_so_far = None
print('Before loop, the smallest number is', smallest_so_far)
for the_num in [9,41,12,3,74,15]:
    if smallest_so_far is None :
        smallest_so_far = the_num
    if the_num < smallest_so_far :
        smallest_so_far = the_num
    print("Samllest number:",smallest_so_far, "Current number:", the_num)
print('After loop, the smallest number is', smallest_so_far)
print()

#Counting in a loop
print('<Counting in a loop>')
count = 0
print('Before loop', count)
for thing in [9,41,12,3,74,15] :
    count += 1
    print(count, ':', thing)
print('We have executed a loop', count, 'times.')
print()

#Summing in a loop
print('<Summing in a loop>')
sum = 0
print('Before loop, the sum is', sum)
for thing in [9,41,12,3,74,15] :
    sum += thing
    print('Sum:' , sum, ', current value:', thing)
print()

#Finding the average in a loop
print('<Finding the average in a loop>')
count = 0
sum = 0
print('<Before loop> count:', count, '/ sum:', sum)
for value in [9,41,12,3,74,15] :
    count += 1
    sum += value
    print(count, ': sum:', sum, ', value:', value)
print('<After loop>: sum:', sum, ', average:', (sum/count))
print()

#Filtering in a loop
print('<Filtering in a loop>')
print('Before loop')
for value in [9,41,12,3,74,15] :
    if(value > 20):
        print('Large number', value)
print('After loop')
print()

#Searching using a Boolean variable
print('<Searching using a Boolean variable: find number 3>')
found = False
print('Before loop')
for value in [9,41,12,3,74,15] :
    if value == 3 :
        found = True
    print('found?', found, value)
print('After loop')
print()
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
