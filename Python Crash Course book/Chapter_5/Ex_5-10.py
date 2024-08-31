current_users = ['Lursi', 'Nona', 'Admin', 'Nona2', 'User5']
new_users = ['user1', 'nona', 'Admin', 'user2', 'newuser']

current_users_lower = [user.lower() for user in current_users]  #lowerd the current users


# now i loop through new users to see if new user lower is in current user lower
# always use in when you want to see inside a list

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")
