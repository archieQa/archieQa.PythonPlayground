# Creating a list with the map function
def square(x):
    return x * x


squares = map(square, range(10))
print(list(squares))


# Using Filtering to return only those which for the statement is true in an iterable

def evens(x):
    return x % 2 == 0


evan = filter(evens, range(10))
print(list(evan))