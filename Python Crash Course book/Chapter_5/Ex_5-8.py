admin_greeting = "Ku je o nona"
normalG = "Hi there"
usernames = ['Lursi', 'Nona', 'Admin', 'Nona2']

username = input('Whats your username? ').strip().lower()

normalize_usernames = [user.lower() for user in usernames]

if username in normalize_usernames:
    if username == 'admin':
        print(admin_greeting)
    else:
        print(normalG)


if username != normalize_usernames:
    print('Your account does not exist')