from enum import Enum


class Klant_status(Enum):
    POTENTIEEL = "potentieel"
    ACTIEF = "actief"
    GEBLOKKEERD = "geblokkeerd"


class Order_status(Enum):
    WORDT_VERZAMELD = "wordt_verzameld"
    VERSTUURD = "verstuurd"
    BACKORDER = "backorder"
    AFGELEVERD = "afgeleverd"


class Factuur_status(Enum):
    OPEN = "open"
    BETAALD = "betaald"
    BETALINGSACHTERSTAND = "betalingsachterstand"
    OVERGEDRAGEN_AAN_INCASSSO = "overgedragen_aan_incasso"


class Levering_status(Enum):
    AFGELEVERD = "afgeleverd"
    GELUKT = "gelukt"
    KLANT_NIET_AANWEZIG = "klant_niet_aanwezig"
    RETOUR_MAGAZIJN = "retour_magazijn"
    ONDERWEG = "onderweg"


class Leverbaarheid_status(Enum):
    LEVERBAAR = "leverbaar"
    NIET_LEVERBAAR = "niet_leverbaar"


class Voorraad_status(Enum):
    OP_VOORRAAD = "op_voorraad"
    ONDER_MINIMUM = "onder_minimum"
    NIET_OP_VOORRAAD = "niet_op_voorraad"

class Robot_status(Enum):
    BESCHIKBAAR = "beschikbaar"
    VERZAMELEN = "VERZAMELEN"

class Verzamelbak_status(Enum):
    LEEG = "beschikbaar"
    IN_GEBRUIK = "VERZAMELEN"
    VOL = 'vol'
    BIJ_DISTRIBUTIE = 'bij distributie'

class Koerier_Status(Enum):
    BESCHIKBAAR = 1
    ONBESCHIKBAAR = 2

class Koerier_Regio(Enum):
    NOORD = 1
    ZUID = 2
    OOST = 3
    WEST = 4

class Rol(Enum):
    KOOIER = 1
    VERKOOP = 2
    ADMINISTRATIE = 3


class Adres:
    def __init__(self, straat, huisnummer, postcode, plaats):
        pass


class Contactpersoon:
    def __init__(self, naam, email, telefoonnummer):
        pass


class Klant:
    def __init__(self, klant_id, bedrijfsnaam, jaaromzet, status: Klant_status):
        self.klant_id = klant_id
        self.bedrijfsnaam = bedrijfsnaam
        self.jaaromzet = jaaromzet
        self.status = status


class Product:
    def __init__(self, product_id, naam, prijs, voorraad_status: Voorraad_status):
        self.product_id = product_id
        self.naam = naam
        self.prijs = prijs
        self.voorraad_status = voorraad_status


class Leverancier:
    def __init__(self, leverancier_id, naam):
        pass


class ProductLeverancier:
    def __init__(self, product: Product, leverancier: Leverancier, leverbaarheid: Leverbaarheid_status):
        self.product = product
        self.leverancier = leverancier
        self.leverbaarheid = leverbaarheid


class Orderregel:
    def __init__(self, product: Product, aantal: int):
        pass


class Order:
    def __init__(self, order_id, klant: Klant, status: Order_status):
        self.order_id = order_id
        self.klant = klant
        self.status = status

    def bereken_totaalbedrag(self):
        pass

    def update_status(self, status: Order_status):
        self.status = status


class Factuur:
    def __init__(self, factuur_id, order: Order, status: Factuur_status):
        self.factuur_id = factuur_id
        self.order = order
        self.status = status


class Levering:
    def __init__(self, levering_id, order: Order, status: Levering_status):
        self.levering_id = levering_id
        self.order = order
        self.status = status

class Medewerker:
    def __init__(self, medewerker_id: int, telefoonnummer: int, voornaam: str, achternaam: str, email: str, gebruikersnaam: str, wachtwoord: str, status: Koerier_Status, regio: Koerier_Regio, rol: Rol):
        self.medewerker_id = medewerker_id
        self.telefoonnummer = telefoonnummer
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.email = email
        self.gebruikersnaam = gebruikersnaam
        self.wachtwoord = wachtwoord
        self.status = status
        self.regio = regio
        self.rol = rol

    def inloggen(self):
        pass  

class Magazijngang:
    def __init__(self, robot_id: int, gang: int, status: Robot_status):
        pass

class Betaling:
    def __init__(self, betaling_id: int, betaaldatum: str, bedrag: float, factuur_id: Factuur):
        pass

class Distributiehoek:
    def __init__(self, distributie_id: int, verpak_datum: str, verzend_datum: str):
        pass

class Verzamelbak:
    def __init__(self, bak_id: int, barcode: str, capaciteit: str, status: Verzamelbak_status):
        pass

class Picktask:
    def __init__(self, picktask_id: int, order_id: Order, robot_id: Magazijngang, bak_id: Verzamelbak, distributiehoek: Distributiehoek):
        pass