fruits = ['Apple', 'Orange', 'Tomato']
fav_fruit = input('Whats your fav fruit: ').strip().lower()

if fav_fruit in [fruit.lower() for fruit in fruits]:
    print('I have that one ')
else:
    print('I dont have it you should buy it')
