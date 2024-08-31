alien_color = 'Blue'

# we use strip to strip of white spaces and whatever
# we use lower to cross reference all characters in lower


while True:
    choice = input('What color is the alien?\n').strip().lower()
    if choice == alien_color.lower():
        print('good job buddy')
        break
    else:
        print('Nope try again')