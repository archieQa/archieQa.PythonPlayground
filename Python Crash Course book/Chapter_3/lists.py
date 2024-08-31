
fruits = ["apple", "cherry", "orange"]
fruits[0] = "avocado"
fruits.append("apple")
fruits.insert(2, "Strawberry")

del fruits[2]
remove_color = fruits.pop(0)
fruits.remove("cherry")
print("This was removed: " + remove_color)

print(fruits)
