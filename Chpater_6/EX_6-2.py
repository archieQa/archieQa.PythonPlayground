# working with different object in a dictionary

persons = {
    'lursi': {'fav_num': 4},
    'cj': {'fav_num': 5},
    'keni': {'fav_num': 6},
    'nona': {'fav_num': 6},
}

for person, value in persons.items():
    print(f"{person} Favorite number is: {value['fav_num']}")
