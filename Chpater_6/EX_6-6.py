# Favorite language we create 1 list and 1 Dictionary for People and people who have already taken the poll

people = ['lursi', 'CJ', 'Kreny']


taken_the_poll = {
    'lursi': 'Python'
}


for person in people:
    if person in taken_the_poll:
        print(f"Thank you {person.title()} for taking the poll")
    else:
        print(f"Please {person.title()} take the poll")