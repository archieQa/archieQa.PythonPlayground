def fib_generator():
    a, b = 0, 1
    for _ in range(1000):
        yield a
        a, b = b, a + b


fib_gen = fib_generator()

for num in fib_gen:
    print(num)