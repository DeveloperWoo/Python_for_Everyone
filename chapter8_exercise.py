'''
Exercise 8.4
Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words.
For each word on each line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
'''
print("<Exercise 8.4>")

fname = input("Enter file name: ") #romeo.txt
fhandle = open(fname)
newList = list()

for line in fhandle :
    line2 = line.rstrip()
    wordsList = line2.split()
    for word in wordsList :
        if word in newList :
            continue
        else :
            newList.append(word)
newList.sort()
print(newList)

print()

'''
Exercise 8.5
Open the file mbox-short2.txt and read it line by line.
When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line
(i.e. the entire address of the person who sent the message).
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
'''
print("<Exercise 8.5>")

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short2.txt"

fh = open(fname)
lst = list()
count = 0

for line in fh:
    wordsInLine = line.rstrip().split()
    if len(wordsInLine) < 3 or wordsInLine[0] != 'From':
        continue
    print(wordsInLine[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")

'''
Exercise 8.6:
Rewrite the program that prompts the user for a list of numbers and
prints out the maximum and minimum of the numbers at the end when the user enters “done”.
Write the program to store the numbers the user enters in a list
and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0
'''
print("<Exercise 8.6>")

numberList = list()
while True:
    num = input("Enter a number: ")
    if(num == 'done'):
        break
    try:
        number = float(num)
        numberList.append(num)
    except:
        print('Invalid Value')
print('Maximum:', max(numberList))
print('Maximum:', min(numberList))
