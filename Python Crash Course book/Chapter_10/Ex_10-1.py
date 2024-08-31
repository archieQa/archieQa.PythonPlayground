# Write a program that reads a file and prints its contents three different ways:
# reading the entire file at once,
# reading line by line, and storing
# the lines in a list and then printing them.

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

print('\n')

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

print('\n')

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())