# Using While loop to fill a dictionary

responses = {}

active = True

while active:
    name = input("What's your name:")
    response = input("Which mountain would you like to climb? ")
    responses[name] = response

    more = input("Would you like to add more? (y/n)")
    if more == 'y':
        continue
    elif more == 'n':
        active = False
    else:
        active = False

for response, value in responses.items():
    print(response, value)

