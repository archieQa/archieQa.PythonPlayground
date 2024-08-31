
cube_numbers = [x * 3 for x in range(10)]
print(cube_numbers)


# Filtering out all the vowels from a string

stringu = "Hello nona me baba per ikona"
vowels = "aeiouAEIOU"

filtered_string =''.join([char for char in stringu if char not in vowels])
print(filtered_string)
