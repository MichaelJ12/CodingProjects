from enum import Enum

# =====================
# ENUMS
# =====================

# Status van een klant
class Klant_status(Enum):
    POTENTIEEL = "potentieel"
    ACTIEF = "actief"
    GEBLOKKEERD = "geblokkeerd"

# Status van een order
class Order_status(Enum):
    WORDT_VERZAMELD = "wordt_verzameld"
    VERSTUURD = "verstuurd"
    BACKORDER = "backorder"
    AFGELEVERD = "afgeleverd"

# Status van een factuur
class Factuur_status(Enum):
    OPEN = "open"
    BETAALD = "betaald"
    BETALINGSACHTERSTAND = "betalingsachterstand"
    OVERGEDRAGEN_AAN_INCASSSO = "overgedragen_aan_incasso"

# Status van een levering
class Levering_status(Enum):
    AFGELEVERD = "afgeleverd"
    GELUKT = "gelukt"
    KLANT_NIET_AANWEZIG = "klant_niet_aanwezig"
    RETOUR_MAGAZIJN = "retour_magazijn"
    ONDERWEG = "onderweg"

# Leverbaarheid van een product
class Leverbaarheid_status(Enum):
    LEVERBAAR = "leverbaar"
    NIET_LEVERBAAR = "niet_leverbaar"

# Voorraadstatus van een product
class Voorraad_status(Enum):
    OP_VOORRAAD = "op_voorraad"
    ONDER_MINIMUM = "onder_minimum"
    NIET_OP_VOORRAAD = "niet_op_voorraad"

# Status van een robot in het magazijn
class Robot_status(Enum):
    BESCHIKBAAR = "beschikbaar"
    VERZAMELEN = "VERZAMELEN"

# Status van een verzamelbak
class Verzamelbak_status(Enum):
    LEEG = "beschikbaar"
    IN_GEBRUIK = "VERZAMELEN"
    VOL = 'vol'
    BIJ_DISTRIBUTIE = 'bij distributie'

# Status van een koerier
class Koerier_Status(Enum):
    BESCHIKBAAR = 1
    ONBESCHIKBAAR = 2

# Regio waarin een koerier actief is
class Koerier_Regio(Enum):
    NOORD = 1
    ZUID = 2
    OOST = 3
    WEST = 4

# Rol van een medewerker
class Rol(Enum):
    KOOIER = 1
    VERKOOP = 2
    ADMINISTRATIE = 3


# =====================
# KLASSEN
# =====================

# Adres van een klant of leverancier
class Adres:
    def __init__(self, straat, huisnummer, postcode, plaats):
        # Sla adresgegevens op
        pass

# Contactpersoon bij een klant of leverancier
class Contactpersoon:
    def __init__(self, naam, email, telefoonnummer):
        # Sla contactinformatie op
        pass

# Klant van het bedrijf
class Klant:
    def __init__(self, klant_id, bedrijfsnaam, jaaromzet, status: Klant_status):
        self.klant_id = klant_id
        self.bedrijfsnaam = bedrijfsnaam
        self.jaaromzet = jaaromzet
        self.status = status
        # Eventueel: adres, contactpersonen toevoegen

# Product dat verkocht kan worden
class Product:
    def __init__(self, product_id, naam, prijs, voorraad_status: Voorraad_status):
        self.product_id = product_id
        self.naam = naam
        self.prijs = prijs
        self.voorraad_status = voorraad_status

# Leverancier van producten
class Leverancier:
    def __init__(self, leverancier_id, naam):
        # Sla leverancierinformatie op
        pass

# Koppeling tussen product en leverancier
class ProductLeverancier:
    def __init__(self, product: Product, leverancier: Leverancier, leverbaarheid: Leverbaarheid_status):
        self.product = product
        self.leverancier = leverancier
        self.leverbaarheid = leverbaarheid

# Een regel binnen een order (product + aantal)
class Orderregel:
    def __init__(self, product: Product, aantal: int):
        # Houdt bij welk product en hoeveel er besteld is
        pass

# Order van een klant
class Order:
    def __init__(self, order_id, klant: Klant, status: Order_status):
        self.order_id = order_id
        self.klant = klant
        self.status = status
        # Eventueel: lijst van Orderregels toevoegen

    # Bereken totaalbedrag van de order
    def bereken_totaalbedrag(self):
        pass

    # Update de status van de order
    def update_status(self, status: Order_status):
        self.status = status

# Factuur gekoppeld aan een order
class Factuur:
    def __init__(self, factuur_id, order: Order, status: Factuur_status):
        self.factuur_id = factuur_id
        self.order = order
        self.status = status

# Levering gekoppeld aan een order
class Levering:
    def __init__(self, levering_id, order: Order, status: Levering_status):
        self.levering_id = levering_id
        self.order = order
        self.status = status

# Medewerker van het bedrijf
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

    # Inloggen (nog te implementeren)
    def inlog(self):
        pass  

# Magazijngang waarin een robot werkt
class Magazijngang:
    def __init__(self, robot_id: int, gang: int, status: Robot_status):
        # Houdt bij welke robot in welke gang actief is en wat de status is
        pass

# Betaling voor een factuur
class Betaling:
    def __init__(self, betaling_id: int, betaaldatum: str, bedrag: float, factuur_id: Factuur):
        pass

# Distributiehoek voor het verzamelen en verzenden van orders
class Distributiehoek:
    def __init__(self, distributie_id: int, verpak_datum: str, verzend_datum: str):
        pass

# Verzamelbak die door robots gebruikt wordt
class Verzamelbak:
    def __init__(self, bak_id: int, barcode: str, capaciteit: str, status: Verzamelbak_status):
        pass

# Picktask: taak voor een robot om producten te verzamelen
class Picktask:
    def __init__(self, picktask_id: int, order_id: Order, robot_id: Magazijngang, bak_id: Verzamelbak, distributiehoek: Distributiehoek):
        pass
