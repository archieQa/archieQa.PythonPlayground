
name = input('Whats your name? ')

with open('namefile.txt', 'w') as file:
    file.write(name)