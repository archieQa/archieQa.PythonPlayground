# modify a file

with open('pi_digits.txt', 'r') as file:
    contents = file.read()

    modified_content = contents.replace('Nona', 'baba')

    print(modified_content)
