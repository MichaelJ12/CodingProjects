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
        # return f" Status: {self.status.name}"

class Leverbaarheid_Status(Enum):
    NIET_LEVERBAAR = 1
    LEVERBAAR = 2

class Product_Leverancier(object):
    def __init__(self, product: str, leverancier: str, prijs: float, leverbaarheid_status: Leverbaarheid_Status) -> None:
        self.product = product
        self.leverancier = leverancier
        self.prijs = prijs
        self.leverbaarheid_status = leverbaarheid_status

class Inkoop_Proces(object):
    def __init__(self, producten: list, leveranciers: list) -> None:
        self.producten = producten
        self.leveranciers = leveranciers
        self.onder_min = []
    
    def controleer_voorraad(self):
        for product in self.producten:
            if product.status == Voorraad_status.ONDER_MINIMUM:
                self.onder_min.append(product)
                
        for minimum in self.onder_min:
            print(f"{minimum}")        
                
                

    def start_inkopen(self):
        for _ in self.leveranciers:
            print(f"info: {self.leveranciers}")

if __name__ == '__main__':

    p1 = Product(1, "Paracetamol", 2.55, 100, 250, Voorraad_status.OP_VOORRAAD)
    p2 = Product(2, "Ibuprofen", 3.10, 80, 60, Voorraad_status.ONDER_MINIMUM)
    p3 = Product(3, "Amoxicilline", 12.99, 50, 0, Voorraad_status.NIET_OP_VOORRAAD)
    p4 = Product(4, "Aspirine", 2.80, 120, 130, Voorraad_status.OP_VOORRAAD)
    p5 = Product(5, "Insuline", 45.00, 30, 10, Voorraad_status.ONDER_MINIMUM)

    pl1 = Product_Leverancier("Paracetamol", "PharmaSupply BV", 1.80, Leverbaarheid_Status.LEVERBAAR)
    pl2 = Product_Leverancier("Insuline", "MedicoGroothandel", 5.40, Leverbaarheid_Status.LEVERBAAR)
    pl3 = Product_Leverancier("Ibuprofen", "HealthCore NV", 2.10, Leverbaarheid_Status.NIET_LEVERBAAR)
    pl4 = Product_Leverancier("Aspirine", "CheapMeds", 1.95, Leverbaarheid_Status.LEVERBAAR)
    pl5 = Product_Leverancier("Amoxicilline", "BioPharm", 10.50, Leverbaarheid_Status.NIET_LEVERBAAR)

    producten = [p1,p2,p3,p4,p5]
    leveranciers = [pl1,pl2,pl3,pl4,pl5]

    inkoop = Inkoop_Proces(producten, leveranciers) 


  
    inkoop.controleer_voorraad()
  