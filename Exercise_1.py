# Exercise 1
class Soda:

    def __init__(self, name):
        self.name = name

    def exam(self):
        if self.name == "":
            print("У вас обычная газировка")
        else:
            print(f"Ваша газировка имеет {self.name} вкус")


flavor = input("Введите вкус газировки: ")
name = Soda(flavor)
name.exam()
