# Input how many people in the dinner group, and then check if more than 8

people_in_group = int(input("How many people in group\n"))

if people_in_group <= 7:
    print("You are welcome and the table is ready")
else:
    print('Im sorry but you have to wait')