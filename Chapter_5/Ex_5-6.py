# A program that determent's a persons stage in life based on age
kid = 10
teen = 15
adult = 20
grown = 50
grandpa = 70
Persons_age = int(input("Enter your age please: "))

if Persons_age <= kid:
    print(" You a kid")
elif Persons_age <= teen:
    print("You a teen ")
elif adult <= Persons_age < grown:
    print("You a adult ")
elif Persons_age <= grown:
    print("You a grown ")
elif Persons_age <= grandpa:
    print("You a grandpa ")
else:
    print("you have a lot of wisdom")