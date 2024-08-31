# Moving items in lists from one to the other

unconfirmed_list = ['Lursi', 'Cj', 'Kreny ']

confirmed_list = []


while unconfirmed_list:
    current_user = unconfirmed_list.pop()
    print(f"Verifying the user {current_user}")
    confirmed_list.append(current_user)

for person in confirmed_list:
    print(person)

