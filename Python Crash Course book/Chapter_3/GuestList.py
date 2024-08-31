guests = ['Lursi', 'CJ', 'Keni']

guests.append('Nona')
guests.insert(0, 'Joni')


guests.remove('Lursi')

print("The guests are: ")
for index, guest in enumerate(guests, start=1):
    print(f'{index} - {guest}')