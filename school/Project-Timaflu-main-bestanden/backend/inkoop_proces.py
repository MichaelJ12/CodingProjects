from enum import Enum

# Enum voor de voorraadstatus van een product
class Voorraad_status(Enum):
    OP_VOORRAAD = 1
    ONDER_MINIMUM = 2
    NIET_OP_VOORRAAD = 3

# Klasse voor een Product
class Product(object):
    def __init__(self, product_id: int, naam: str, prijs: float, minimum_voorraad: int, hoeveelheid: int, status: Voorraad_status) -> None:
        self.product_id = product_id
        self.naam = naam
        self.prijs = prijs
        self.minimum_voorraad = minimum_voorraad
        self.hoeveelheid = hoeveelheid
        self.status = status

    def __str__(self) -> str:
        # Geeft een leesbare representatie van het product
        return f"Naam: {self.naam} | Minimum voorraad: {self.minimum_voorraad} | Huidige hoeveelheid: {self.hoeveelheid} | Status: {self.status.name}"

# Enum voor leverbaarheid van een product bij een leverancier
class Leverbaarheid_Status(Enum):
    NIET_LEVERBAAR = 1
    LEVERBAAR = 2

# Klasse voor Product gekoppeld aan een leverancier
class Product_Leverancier(object):
    def __init__(self, product: Product, leverancier: str, prijs: float, leverbaarheid_status: Leverbaarheid_Status) -> None:
        self.product = product
        self.leverancier = leverancier
        self.prijs = prijs
        self.leverbaarheid_status = leverbaarheid_status

    def __str__(self) -> str:
        # Geeft een overzicht van product + leverancier + prijs + leverbaarheid
        return f"Product naam: {self.product.naam} | Leverancier: {self.leverancier} | Prijs: €{self.prijs:.2f} | Status: {self.leverbaarheid_status.name}"

# Inkoopproces: controle en bestellen van producten
class Inkoop_Proces(object):
    def __init__(self, producten: list, leveranciers: list) -> None:
        self.producten = producten
        self.leveranciers = leveranciers
        self.onder_minimim = []  # lijst met producten onder minimum voorraad
        self.cheapest = []       # (optioneel) lijst voor goedkoopste leverancier
    
    # Controleer welke producten onder minimum voorraad zitten
    def controleer_voorraad(self):
        for product in self.producten:
            if product.status == Voorraad_status.ONDER_MINIMUM:
                self.onder_minimim.append(product)
                
        # Print producten onder minimum
        for minimum in self.onder_minimim:
            print(f"{minimum}")
        print("_" * 50)  

    # Start inkoopproces: bestel producten bij de goedkoopste leverbare leverancier
    def start_inkopen(self):
        for product in self.onder_minimim:
            goedkoopste_leverancier = None
            laagste_prijs = None
            # Doorloop alle leveranciers om de goedkoopste leverbare te vinden
            for leverancier in self.leveranciers:
                if leverancier.product == product and leverancier.leverbaarheid_status == Leverbaarheid_Status.LEVERBAAR: 
                    if goedkoopste_leverancier is None or leverancier.prijs < laagste_prijs:   
                        goedkoopste_leverancier = leverancier
                        laagste_prijs = leverancier.prijs
            # Print resultaat van de inkoop
            if goedkoopste_leverancier:
                print(f"Product {product.naam} wordt gekocht van {goedkoopste_leverancier.leverancier} met de prijs €{laagste_prijs:.2f}")    
            else: 
                print(f"Geen beschikbare leverancier voor dit product {product.naam}")


if __name__ == '__main__':
    # Dummy producten
    p1 = Product(1, "Paracetamol", 2.55, 100, 250, Voorraad_status.OP_VOORRAAD)
    p2 = Product(2, "Ibuprofen", 3.10, 80, 60, Voorraad_status.ONDER_MINIMUM)
    p3 = Product(3, "Amoxicilline", 12.99, 50, 0, Voorraad_status.NIET_OP_VOORRAAD)
    p4 = Product(4, "Aspirine", 2.80, 120, 130, Voorraad_status.OP_VOORRAAD)
    p5 = Product(5, "Insuline", 45.00, 30, 10, Voorraad_status.ONDER_MINIMUM)

    # Dummy leveranciers
    pl1 = Product_Leverancier(p1, "PharmaSupply BV", 1.80, Leverbaarheid_Status.LEVERBAAR)
    pl2 = Product_Leverancier(p5, "MedicoGroothandel", 5.40, Leverbaarheid_Status.LEVERBAAR)
    pl3 = Product_Leverancier(p2, "HealthCore NV", 2.10, Leverbaarheid_Status.NIET_LEVERBAAR)
    pl4 = Product_Leverancier(p4, "CheapMeds", 1.95, Leverbaarheid_Status.LEVERBAAR)
    pl5 = Product_Leverancier(p3, "BioPharm", 10.50, Leverbaarheid_Status.NIET_LEVERBAAR)
    pl6 = Product_Leverancier(p2, "MedicoGroothandel", 2.40, Leverbaarheid_Status.LEVERBAAR)
    pl7 = Product_Leverancier(p2, "PharmaSupply BV", 1.10, Leverbaarheid_Status.LEVERBAAR)
    pl8 = Product_Leverancier(p2, "CheapMeds", 2.10, Leverbaarheid_Status.LEVERBAAR)
    pl9 = Product_Leverancier(p2, "HealthPlus", 2.30, Leverbaarheid_Status.LEVERBAAR)
    pl10 = Product_Leverancier(p2, "EuroPharma", 2.15, Leverbaarheid_Status.LEVERBAAR)

    producten = [p1,p2,p3,p4,p5]
    leveranciers = [pl1,pl2,pl3,pl4,pl5,pl6,pl7,pl8,pl9,pl10]

    # Inkoopproces starten
    inkoop = Inkoop_Proces(producten, leveranciers) 
    inkoop.controleer_voorraad()
    inkoop.start_inkopen()
