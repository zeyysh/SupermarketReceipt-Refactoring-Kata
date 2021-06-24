from enum import Enum


class Product:
    def __init__(self, name, weight, height, length, sku):
        self.sku = sku
        self.length = length
        self.height = height
        self.weight = weight
        self.name = name


class ProductSale:
    def __init__(self, price, unit):
        self.unit = unit
        self.price = price


class ProductQuantity:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class ProductUnit(Enum):
    EACH = 1
    KILO = 2


class SpecialOfferType(Enum):
    THREE_FOR_TWO = 1
    TEN_PERCENT_DISCOUNT = 2
    TWO_FOR_AMOUNT = 3
    FIVE_FOR_AMOUNT = 4

class Offer:
    def __init__(self, offer_type, product, argument):
        self.offer_type = offer_type
        self.product = product
        self.argument = argument


class Discount:
    def __init__(self, product, start_date, end_date, min_quantity, max_quantity, discount_amount, discount_percent):
        self.end_date = end_date
        self.min_quantity = min_quantity
        self.max_quantity = max_quantity
        self.discount_percent = discount_percent
        self.product = product
        self.discount_amount = discount_amount
