#Exercise 1: Write your pay computation to give the employee
#1.5times the hourly rate for hours worked above 40 hours.

#Ent#er Hours: 45
#Enter Rate: 10
#Pay: 475.0
print("<Exercise 1>")

hrs = input("Enter Hours:")
hrsInNum = float(hrs)
rate = input("Enter Rate:")
rateInNum = float(rate)
rateForOverTime = rateInNum * 1.5

if (hrsInNum > 40):
    pay = (40 * rateInNum) + ((hrsInNum-40)*(rateForOverTime))
else:
    pay = hrsInNum * rateInNum
print("Pay:", pay)


#Exercise 2: Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program. The following shows two executions of the program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input
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
            pay2 = (40 * rateInNum2) + ((hrsInNum2 - 40)*(rateInNum2 * 1.5))
        else:
            pay2 = hrsInNum2 * rateInNum2
        print("Pay:", pay2)
