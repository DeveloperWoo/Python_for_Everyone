'''
Exercise 6.5:
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
'''
print("<Exercise 6.5>")

text = "X-DSPAM-Confidence:    0.8475";
spaceEnd = text.find(' ')
the_num = text[spaceEnd:]
the_numInFloat = float(the_num)
print(the_numInFloat) #0.8475
