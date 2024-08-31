cart = ["Milk", "Eggs", "Coffe", "Bread"]
cart.append("butter")
cart.append("cheese")

cart.remove("Eggs")
del cart[0]

cart.insert(0, 'Drink')
cart.insert(1, 'Book')
cart.sort()

print("Items in Cart: ")
for Item in cart:
    print(f"- {Item}")

