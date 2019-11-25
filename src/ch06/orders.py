from typing import List


class LineItem:

    def __init__(self, product: str, quantity: int, price: float):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:

    def __init__(self, customer: str, cart: List[LineItem], promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        return sum(item.total() for item in self.cart)

    def due(self):
        if self.promotion is None:
            return
        discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'

