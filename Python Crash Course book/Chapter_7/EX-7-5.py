# Write a loop that asks for age and tell the price depending on age

price_kid = 5
price_teen = 10
price_grow = 20


active = True

while active:
    age = int(input('What is your age? '))
    if age <= 5:
        print(f"You need to pay {price_kid}$")
    elif age <= 15:
        print(f"You need to pay {price_teen}$")
    elif age <= 60:
        print(f"You need to pay {price_grow}$")
    else:
        print("You to old for this homie ")

    break
