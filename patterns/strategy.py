from abc import ABC, abstractmethod
from decimal import Decimal

class User:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __str__(self):
        return self.name

class LineItem:
    def __init__(self, product_id, quantity, price):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self, user, cart, promotion):
        self.user = user
        self.cart = cart
        self.promotion = promotion

    def total(self):
        total = Decimal('0')
        for item in self.cart:
            total += item.total()
        return total

    def due(self):
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __str__(self):
        return f"<Order total: {self.total()} due: {self.due()}>"

class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
       """Returns discount as a positive amount"""

class PointsPromo(Promotion):

    def discount(self, order):
        rate = Decimal('0.05')
        if order.user.points >= 1000:
            return order.total() * rate
        return Decimal('0')

class BulkItemPromo(Promotion):
    def discount(self, order):
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal('0.1')
        return discount


class LargeOrderPromo(Promotion):
    def discount(self, order):
        distinct_item = {item.product_id for item in order.cart}
        if len(distinct_item) >= 10:
            return order.total() * Decimal('0.07')
        return Decimal(0)


joe = User('John Doe', 0)
ann = User('Ann Smith', 1100)
cart = [LineItem('banana', 4, Decimal('.5')),
        LineItem('apple',10, Decimal('1.5')),
        LineItem('watermelon', 5, Decimal(5))]

print(Order(joe, cart, PointsPromo()))
print(Order(ann, cart, PointsPromo()))
banana_cart = [LineItem('banana', 30, Decimal('0.5'))
               , LineItem('apple', 10, Decimal('1.5'))]
print(Order(joe, banana_cart, BulkItemPromo()))

long_cart = [LineItem(str(i), 1, Decimal(1)) for i in range(10)]

print(Order(joe, long_cart, LargeOrderPromo()))
print(Order(joe, cart, LargeOrderPromo()))

