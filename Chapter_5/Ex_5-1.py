number = input('Enter Guessed number:')


if number == 10:
    print("Correct")
elif number == 20:
    print('You are not correct go lower')
elif number <= str(15):
    print('you on the right track go a bit lower ')
elif number <= str(9):
    print('you on the right track go a bit higher ')
else:
    print('fuck you ')