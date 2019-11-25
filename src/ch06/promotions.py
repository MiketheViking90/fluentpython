from abc import ABC, abstractmethod

from src.ch06.orders import Order


class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        """Return discount"""

class BulkItemPromotion(Promotion):
    """10% discount for each LineItem with 20 or more units"""

    def discount(self, order: Order):
        bulk_items = [item for item in order.cart if item.quantity > 20]
        discount = 0
        for bulk_item in bulk_items:
            discount += (bulk_item.total() * .1)
        return discount

class LargeCartPromotion(Promotion):
    """7% discount for orders with 10 or more distinct items"""

    def discount(self, order: Order):
        is_large_cart = len(order.cart) >= 2
        if is_large_cart:
            return order.total() * .07
        else:
            return 0