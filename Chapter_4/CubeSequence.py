numbers = [x**3 for x in range(0, 10)]

numbers_1_sliced = numbers[0:3]
numbers_2_sliced = numbers[3:6]
numbers_3_sliced = numbers[6:10]

print(numbers_1_sliced, numbers_2_sliced,numbers_3_sliced)

for number in numbers:
    print(number)