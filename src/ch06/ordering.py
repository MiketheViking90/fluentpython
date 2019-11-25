import functools
import operator

from src.ch06.orders import LineItem, Order

def bulk_item_promotion(order: Order):
    bulk_total = functools.reduce(operator.mul,
        [item.total() for item in order.cart if item.quantity > 20])
    print(bulk_total)
    return bulk_total * .1

def large_cart_promotion(order: Order):
    if len(order.cart) >= 2:
        return .07 * order.total()
    return 0



cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('butter', 25, 7.4)]
order1 = Order('joe', cart, bulk_item_promotion)
due1 = order1.due()
total1 = order1.total()
print(due1, total1)

order2 = Order('joe', cart, large_cart_promotion)
due2 = order2.due()
total2 = order2.total()
print(due2, total2)
