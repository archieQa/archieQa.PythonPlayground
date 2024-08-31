class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempt = 0

    def login_attempt1(self, number):
        self.login_attempt = number
        print(number)

    def add_login_attempt(self, number_added):
        self.login_attempt += number_added
        print(self.login_attempt)
    def show_data(self):
        print(f"{self.first_name}'s Data:\n -{self.first_name} -{self.last_name} -{self.age}")


user_arsi = User('Arsi', 'Qamo', 20)
user_arsi.show_data()
user_arsi.login_attempt1(5)
user_arsi.add_login_attempt(9)


