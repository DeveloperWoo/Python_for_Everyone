'''
Exercise 1:
Write your pay computation to give the employee
1.5times the hourly rate for hours worked above 40 hours.
<output>
Ent#er Hours: 45
Enter Rate: 10
Pay: 475.0
'''
print("<Exercise 1>")

hrs = input("Enter Hours:")
hrsInNum = float(hrs)
rate = input("Enter Rate:")
rateInNum = float(rate)
rateForOverTime = rateInNum * 1.5

if (hrsInNum > 40):
    print('Overtime')
    pay = (40 * rateInNum) + ((hrsInNum-40)*(rateForOverTime))
else:
    print('Regular')
    pay = hrsInNum * rateInNum
print("Pay:", pay)


'''
Exercise 2:
Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the program:
<output>
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input
'''

print("<Exercise 2>")

hrs2 = input("Enter Hours:")
try:
    hrsInNum2 = float(hrs2)
except:
    print("Error, please enter numeric input")
    hrsInNum2 = -1

if(hrsInNum2 > 0):
    rate2 = input("Enter Rate:")
    try:
        rateInNum2 = float(rate2)
    except:
        print("Error, please enter numeric input")
        rateInNum2 = -1
    if(rateInNum2 > 0) :
        if (hrsInNum2 > 40):
            print('Overtime')
            pay2 = (40 * rateInNum2) + ((hrsInNum2 - 40)*(rateInNum2 * 1.5))
        else:
            print('Regular')
            pay2 = hrsInNum2 * rateInNum2
        print("Pay:", pay2)

'''
Exercise 3:
Write a program to prompt for a score between 0.0 and
1.0. If the score is out of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table:
<output>
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
'''
print("<Exercise 3>")
while(True):
    try:
        score = input("Enter score:")
        scoreInNum = float(score)
        if((scoreInNum >= 0.0) & (scoreInNum <= 1.0)):
            if((scoreInNum >= 0.9)):
                print('A')
            elif(scoreInNum >= 0.8):
                print('B')
            elif(scoreInNum >= 0.7):
                print('C')
            elif(scoreInNum >= 0.6):
                print('D')
            else:
                print('F')
        else:
            print("Bad score")
    except:
        print("Bad score")
