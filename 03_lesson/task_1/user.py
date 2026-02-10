class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayFirstName(self):
        print(f"Имя: {self.first_name}")

    def sayLastName(self):
        print(f"Фамилия: {self.last_name}")

    def sayFirsLastName(self):
        print(f"Имя и Фамилия: {self.first_name} {self.last_name}")
