class Klant(object):
    def __init__(self, name, adres, residence) -> None:
        self.klant_id = None
        self.name = name
        self.adres = adres
        self.residence = residence
        
    def print(self) -> None:
        pass


class Product(object):
    def __init__(self, name, price, btw, stock) -> None:
        self.name = name
        self.price = price 
        self.btw = btw
        self.stock = stock 
        
    def print(self) -> None:
        pass

class Order(object):
    def __init__(self) -> None:
        self.order_nr = None
        self.products = []

    def add_product(self) -> None:
        pass

    def receipt(self) -> None:
        pass


if __name__ == "__main__":
    pass