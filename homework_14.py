#1
#class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         if amount > 2500:
#             print(f"{amount} laris shetana sheudzlebelia limit is 2500")
#         elif amount <= 0:
#             print("please, enter dadebiti tanxa")
#         else:
#             self.balance += amount
#             print(f"it was succesfully added {amount} lari")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print(f"ypou dont have enough cash you are broke: {self.balance} ")
#         elif amount <= 0:
#             print("please enter correct ")
#         else:
#             self.balance -= amount
#             print(f"angarishidan gatanilia {amount}lari")
#
#     def display_balance(self):
#         print(f"mflobeli: {self.owner} | nashti: {self.balance} lari")

#2
import math
class Shape:
    def describe(self):
        print("I am a shape")
class Polygon(Shape):
    def __init__(self, sides):
        self.sides = sides
class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__(sides=3)
        self.a = a
        self.b = b
        self.c = c
    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area
my_triangle = Triangle(3, 4, 5)
my_triangle.describe()
print(f"samkutxedis fartobi: {my_triangle.calculate_area()}")
