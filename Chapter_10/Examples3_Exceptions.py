# Using Try Except blocks to handle errors

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2

except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Error")
else:
    print(result)
finally:
    print('Final block that executes no matter what')