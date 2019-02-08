'''
Exercise 7.1
Write a program to read through a file and print the contents of the file (line by line) all in upper case.
Executing the program will look as follows:

Enter a file name: mbox-short1.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500
'''
print("<Exercise 7.1>")

fname = input("Enter file name: ")
fhandle = open(fname)

for line in fhandle:
    line_after_rstrip = line.rstrip()
    print(line_after_rstrip.upper())

print()

'''
Exercise 7.2
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
When you are testing below enter mbox-short2.txt as the file name.
'''
print("<Exercise 7.2>")

fname = input("Enter file name: ")
fhandle = open(fname)

values = 0
count = 0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    spPos = line.find(' ')
    value = line[(spPos+1):]
    valueInFloat = float(value)
    values = values + valueInFloat
    count += 1
print("Average spam confidence:", values/count)

'''
Exercise 7.3
Sometimes when programmers get bored or want to have a bit of fun,
they add a harmless Easter Egg to their program.
Modify the program that prompts the user for the file name so that it prints a funny message
when the user types in the exact file name “na na boo boo”.
The program should behave normally for all other files which exist and don’t exist.
Here is a sample execution of the program:

>>Enter the file name: mbox-short2.txt
There were 1909 subject lines in mbox.txt
>>Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt
>>Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!

'''
print("<Exercise 7.3>")

fname = input("Enter file name: ")
try:
    if(fname == 'na na boo boo'):
        print("NA NA BOO BOO TO YOU - You have been punk'd")
    else:
        fhandle = open(fname)
        count = 0
        for line in fhandle:
            count += 1
        print('There were', count, 'subject lines in', fname)
except:
    print('File cannot be opened:',  fname)
