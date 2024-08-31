# Write a program that prompts for two numbers.
# Add them together and print the result.
# Handle the exception if the user enters something other than a number.
import json

try:
    x = int(input('Add first num: '))
    y = int(input('Add 2nd num: '))
    z = x + y
    print(z)
except ValueError:
    print('It did not work cuz..')
else:
    x = int(input('Add first num: '))
    y = int(input('Add 2nd num: '))
    z = x - y
    print(z)