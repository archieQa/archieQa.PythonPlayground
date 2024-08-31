def greeting_everyone(*usernames):
    for user in usernames:
        print(f'Hello {user}')


greeting_everyone('Lursi', 'Nona')
