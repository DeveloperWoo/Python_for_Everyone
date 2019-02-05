#Chapter 2

#Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them
#Enter your name: Chuck
#Hello Chuck
print("<Exercise 2>")

name = input('Enter your name: ')
print('Hello', name)

print()

#Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25
print("<Exercise 3>")

hours = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))
pay = hours * rate
print("Pay: ", pay)

print()

#Exercise 4: Assume that we execute the following assignment statements:
width = 17
height = 12.0
print("<Exercise 4>")

print(width/2) #8.5
print(type(width/2)) #<class 'float'>
print(width/2.0) #8.5
print(type(width/2.0)) #<class 'float'>
print(height/2) #6.0
print(type(height/2)) #<class 'float'>
print(1+2*5) #11
print(type(1+2*5)) #<class 'int'>

print()

#Exercise 5: Write a program which prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit, and print out the converted temperature.
#formula: (0°C × 9/5) + 32 = 32°F

print("<Exercise 5>")

tempInCelsius = float(input("Enter a Celsius temperature: "))
tempInFahrenheit = (tempInCelsius * 9/5) + 32
print("Celsius temperature:", tempInCelsius )
print("Fahrenheit temperature:", tempInFahrenheit )
