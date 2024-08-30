# Dictionary containing 3 major rivers and looping throw it 3 times

rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'yangtze': 'China'
}

for river, value in rivers.items():
    print(f"The {river.title()} runs through {value.title()}")


for value in rivers.values():
    print(value)