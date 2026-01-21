from enum import Enum

class Voorraad_status(Enum):
    OP_VOORRAAD = 1
    ONDER_MINIMUM = 2
    NIET_OP_VOORRAAD = 3

class Product(object):
    def __init__(self, product_id: int, naam: str, prijs: float, minimum_voorraad: int, hoeveelheid: int, status: Voorraad_status) -> None:
        self.product_id = product_id
        self.naam = naam
        self.prijs = prijs
        self.minimum_voorraad = minimum_voorraad
        self.hoeveelheid = hoeveelheid
        self.status = status

    def __str__(self) -> str:
        return f"Naam: {self.naam} | Minimum voorraad: {self.minimum_voorraad} | Huidige hoeveelheid: {self.hoeveelheid} | Status: {self.status.name}"

    def toon_info(self) -> None:
        print(f"Product ID: {self.product_id}")
        print(f"Naam: {self.naam}")
        print(f"Prijs: €{round(self.prijs, 2)}")
        print(f"Minimum voorraad: {self.minimum_voorraad}")
        print(f"Huidige hoeveelheid: {self.hoeveelheid}")
        print(f"Status: {self.status.name}")
        print("-" * 30)

class Leverbaarheid_Status(Enum):
    NIET_LEVERBAAR = 1
    LEVERBAAR = 2

class Product_Leverancier(object):
    def __init__(self, product: str, leverancier: str, prijs: float, leverbaarheid_status: Leverbaarheid_Status) -> None:
        self.product = product
        self.leverancier = leverancier
        self.prijs = prijs
        self.leverbaarheid_status = leverbaarheid_status

    def toon_info(self) -> None:
        print(f"Product: {self.product}")
        print(f"Leverancier: {self.leverancier}")
        print(f"Inkoopprijs: €{self.prijs}")
        print(f"Leverbaar: {self.leverbaarheid_status.name}")
        print("=" * 30)    

class Inkoop_Proces(object):
    def __init__(self, producten: list, leveranciers: list) -> None:
        self.producten = producten
        self.leveranciers = leveranciers

    def controleer_voorraad(self):
        for prodcut in self.producten:
            print(f"info: {prodcut}")

    def start_inkopen(self):
        for _ in self.leveranciers:
            print(f"info: {self.leveranciers}")

