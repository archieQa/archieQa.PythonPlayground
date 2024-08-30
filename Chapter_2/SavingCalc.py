
name = "Luars"
salary = 932
rent = 500
food = 200
utilities = 50
saving_rate = 0.1  # 10% of the salary

expenses = salary - rent - food - utilities
remaining_income = salary - expenses
savings = remaining_income * saving_rate

summary_message = "after expenses you will have " + str(savings) + " This month \n"
print(summary_message)