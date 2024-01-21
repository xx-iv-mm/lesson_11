# Exercise_4
import math as m


class Sphere:
    def __init__(self, rad=1, x=0, y=0, z=0):
        self.rad = rad
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self, rad=1):
        self.rad = rad
        volume = (4 / 3) * m.pi * self.rad ** 3
        print(f"R сферы - {self.rad}")
        print(f"Объём сферы = {volume:.3f} см^3")

    def get_square(self, rad=1):
        self.rad = rad
        value = 4 * m.pi * self.rad ** 2
        print(f"R сферы - {self.rad}")
        print(f"P сферы = {value:.3f} см^3")

    def get_radius(self):
        print(f"Текущий радиус сферы - {self.rad}")

    def get_center(self):
        print(f"Текущие координаты сферы:\nx:{self.x}\ny:{self.y}\nz:{self.z}")

    def set_radius(self, rad=1):
        self.rad = rad


d = Sphere()
d.get_volume(3)
d.get_square(3)
d.get_radius()
d.get_center()
d.set_radius(7)
