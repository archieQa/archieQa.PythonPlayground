# Writing to a file


with open('pi_digits.txt', 'w') as file_object:
    file_object.write('Hello world')


# We can write in the file as append mode "a" to add content without deleting the previous one

with open('pi_digits.txt', 'a') as file_object:
    file_object.write("nona me koka per ikona")