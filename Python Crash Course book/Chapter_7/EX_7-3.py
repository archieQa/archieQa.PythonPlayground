# Number multiple of 10


number = int(input("Please enter a number: "))

if number % 10 == 0:
    print(f"{number} is multiple by 10")
else:
    print(f"Number {number} is not multiple by 10")