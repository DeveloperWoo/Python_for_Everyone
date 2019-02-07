'''
Exercise 4.6:
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.
'''
print("<Exercise 4.6>")

def computepay(h,r):
    if(h <= 40):
        pay = h * r
    else:
        regularPay = 40 * r
        overtimePay = (h-40)*(r*1.5)
        pay = regularPay + overtimePay
    return(pay)

hrs = input("Enter Hours:")
rate = input("Enter rate:")
hrsInNum = float(hrs)
rateInNum = float(rate)

p = computepay(hrsInNum, rateInNum)
print("Pay:", p)

'''
Exercise 7:
Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
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
print("<Exercise 7>")

def computeGrade():
    try:
        score = input("Enter score:")
        scoreInNum = float(score)
        if((scoreInNum >= 0.0) & (scoreInNum <= 1.0)):
            if((scoreInNum >= 0.9)):
                strScore = 'A'
            elif(scoreInNum >= 0.8):
                strScore = 'B'
            elif(scoreInNum >= 0.7):
                strScore = 'C'
            elif(scoreInNum >= 0.6):
                strScore = 'D'
            else:
                strScore = 'F'
        else:
            strScore = "Bad score"
    except:
        strScore = "Bad score"
    return strScore

while(True):
    print(computeGrade())
