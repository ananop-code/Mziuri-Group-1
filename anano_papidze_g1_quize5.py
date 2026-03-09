class Tickets:
    def __init__(self, movie_name, price, amount, language="Geo"):
        self.movie_name = movie_name
        self.price = price
        self.amount = amount
        self.language = language

    def __str__(self):
        print(f"movie: {self.movie_name}, price: {self.price}, amount: {self.amount}, language: {self.language}")
    def __gt__(self, other):
        if other.amount > other.amount:
            return True
        else:
            return False

class Users:
    def __init__(self, user_name, balance):
        self.user_name = user_name
        self.balance = balance

    def __str__(self):
        print(f"user: {self.user_name}, balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"balance is {amount}, new balance: {self.balance}")

    def buy_ticket(self, ticket_obj, amount_tobuy):
        total_price = ticket_obj.price * amount_tobuy
        if total_price <= self.balance:
            self.balance -= total_price
            print(f"balance is now {self.balance}, new balance: {self.balance}")
        if ticket_obj.amount > amount_tobuy:
            print("Not enough amount")
        elif self.balance < total_price:
            print("Not enough balance")
        else:
            self.balance -= total_price
            ticket_obj.amount -= amount_tobuy
            print(f"you bought {amount_tobuy} ticket")

t1 = Tickets("Harry Potter", 20, 10)
user1 = Users("Jasurberki", 20)
user1.deposit(10)
user1.__str__()
user1.buy_ticket(t1, 2)
user1.__str__()
user1.__gt__(user1)
print(user1.balance)
print(user1)
print(t1)
# t1 = Tickets("Harry Potter", 15, 20)
# user1 = Users("jasurberki", 50)
# user1.buy_ticket(t1, 2)
# user1.deposit(100)
# print(user1)
# print(t1)

