# Pizza toppings write a loop that prompts for pizza topping

active = True

while active:
    topping = input(" What topping would you like on your pizza? ")
    print(f"Okay I will add {topping} to your pizza")
    stop = input("Do you want more? Write quit to stop")
    if stop == 'quit':
        active = False
    else:
        continue

