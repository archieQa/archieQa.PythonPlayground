def greeter():
    print("Hello")


greeter()


def greeter1(username):
    print(f"hello {username}")


greeter1("Nona")


def multi(x, y):
    z = x + y
    print(f"The answer is {z}")


multi(1, 2)


def get_formatted_name(firstname, lastname, middle_name=None):
    if middle_name:
        fullname = firstname + lastname + middle_name
    else:
        fullname = firstname + lastname
    return fullname.title()


x = get_formatted_name('Lursi', ' Hart', 'Nona')
print(f'{x}\n')


def build_person(last_name, first_name):
    person = {'first': first_name, 'last': last_name}
    for items in person.values():
        return items


personi = build_person('Qamo', 'Luars')
print(personi)


# passing a list as argument

def passing_list(names):
    for name in names:
        print(f'Hello {name}')


names = ['Lursi', 'Nona']
passing_list(names)


# Working with lists and manipulating lists on a function


def printing_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_module = unprinted_designs.pop()
        print(f'Current process is {current_module}')
        completed_models.append(current_module)


unprinted_design = ['phonecase', 'battery', 'mouse']
completed_models = []


printing_models(unprinted_design, completed_models)
print(f'Completed Modules: {completed_models}')



# Using arbitrary number of arguments

def make_pizza(*toppings):
    print("the following are the toppings:")
    for topping in toppings:
        print(f'{topping}')


make_pizza('qssqsqwsdq', 'qasqdasdas')


# Building a profile with an argument ** that hold multiple keys in a dictionery


def building_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last }
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = building_profile('luars', 'Qamo',
                                location='Germany',
                                year=2003
                                )

print(user_profile)

