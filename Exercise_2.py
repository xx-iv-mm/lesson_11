# Exercise 2
class Math:

    def addition(self, num_1, num_2):
        print(f"{num_1} + {num_2} = {num_1 + num_2}")

    def subtraction(self, num_1, num_2):
        print(f"{num_1} - {num_2} = {num_1 - num_2}")

    def multiplication(self, num_1, num_2):
        print(f"{num_1} * {num_2} = {num_1 * num_2}")

    def division(self, num_1, num_2):
        print(f"{num_1} / {num_2} = {(num_1 / num_2):.2f}")


exam = Math()
exam.addition(4, 1)
exam.subtraction(9, 4)
exam.multiplication(7, 3)
exam.division(36, 9)