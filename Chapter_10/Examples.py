with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())

# with = the file is closed after it has been read
# r.strip = we use rsrtip to read and strip from a file. We strip all the unnesscesery lines

# proccesing a file line by line

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


# Storing lines in the list

with open(filename) as file_object:
    lines = file_object.readline()

for line in lines:
    print(line.rstrip())