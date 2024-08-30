#Task: Write a while loop that prompts users for their name.
# Each time they enter their name,print a greeting and add a line recording
# their visit in a file called guest_book.txt.


while True:
    user = input("Whats your name? ")
    print(f'Hello {user}, nice to meet you')
    with open('guest_book.txt', 'w') as file:
        file.write(f"{user} visited the site.\n")
