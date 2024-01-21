# Exercise_3
class Car:

    def __init__(self, color="Белый", typing="Седан", year="2017"):
        self.color = color
        self.typing = typing
        self.year = year

    def start(self):
        print("Автомобиль запущен!")

    def stop(self):
        print("Автомобиль заглушен!")

    def color_new(self, color):
        self.color = color

    def typing_new(self, typing):
        self.typing = typing

    def year_new(self, year):
        self.year = year

    def display_info(self):
        print(f"\n---Car informations---\n\nColor: {self.color}\nType: {self.typing}\nYear: {self.year}\n")

    def new_display_info(self):
        print(f"\n---New Car informations---\n\nColor: {self.color}\nType: {self.typing}\nYear: {self.year}\n")


x = Car()
x.display_info()
x.start()
x.stop()
x.color_new("Черный")
x.typing_new("Универсал")
x.year_new("2020")
x.new_display_info()