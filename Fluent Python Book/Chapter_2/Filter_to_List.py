# From filterd to list comprehension
numbers = [x for x in range(10) if x > 5]
print(numbers)


# from list comphrehension to filterd

numbers2 = [1,2,3,4,5,6,7,8,9,10]

filtered_nums = list(filter(lambda x: x > 5, numbers2))
print(filtered_nums)