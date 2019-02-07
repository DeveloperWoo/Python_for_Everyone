#Exercise 1: Write your pay computation to give the employee
#1.5times the hourly rate for hours worked above 40 hours.
#Ent#er Hours: 45
#Enter Rate: 10
#Pay: 475.0

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
