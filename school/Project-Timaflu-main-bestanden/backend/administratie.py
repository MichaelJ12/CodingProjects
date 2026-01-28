#ADMINISTRATIE TIMAFLU
from enum import Enum

#STATUS VOOR DE FACTUUR
class Factuur_Status(Enum):
    OPEN = 1
    BETAALD = 2
    OVERGEDRAGEN_AAN_INCASSO = 3
    EERSTE_HERINNERING = 4
    TWEEDE_HERINNERING = 5

class Factuur:
    def __init__(self, factuur_id: int, datum: str, bedrag: int, vervaldatum: str, status: Factuur_Status):
        self.factuur_id = factuur_id
        self.datum = datum
        self.bedrag = bedrag
        self.vervaldatum = vervaldatum
        self.status = status

    def __str__(self):
        return (
            f'Factuur ID: {self.factuur_id} | '
            f'Datum: {self.datum} | '
            f'Bedrag: €{self.bedrag} | '
            f'Vervaldatum: {self.vervaldatum} | '
            f'Status: {self.status.name}'
        )

# STATUS VOOR DE KLANT
class Klant_Status(Enum):
    POTENTIEEL = 1
    ACTIEF = 2
    GEBLOKKEERD = 3

class Klant:
    def __init__(self, klant_id: int, bedrijfsnaam: str, jaaromzet: int, korting: int, status: Klant_Status, factuuradres: int):
        self.klant_id = klant_id
        self.bedrijfsnaam = bedrijfsnaam
        self.jaaromzet = jaaromzet
        self.korting = korting
        self.status = status
        self.factuuradres = factuuradres

class Betaling:
    def __init__(self, betaling_id: int, betaaldatum: str, bedrag: int, factuur: Factuur):
        self.betaling_id = betaling_id
        self.betaaldatum = betaaldatum
        self.bedrag = bedrag
        self.factuur = factuur
        

class Order:
    def __init__(self, order_id: int, totaalbedrag: str, klant_id: int, factuur_id: int):
        self.order_id = order_id
        self.totaalbedrag = totaalbedrag
        self.klant_id = klant_id
        self.factuur_id = factuur_id

class Administratie_service:
    def __init__(self, facturen: list, klanten: list, orders: list):
        self.facturen = facturen
        self.facturen_open = []

        self.klanten = klanten
        self.orders = orders

    def controleer_open_facturen(self):
        for factuur in self.facturen:
            if factuur.status == Factuur_Status.OPEN:
                self.facturen_open.append(factuur)
                print(f'Dit is een factuur: {factuur}')
                print('Dit factuur heeft de status: OPEN ^^^^^^^')

    def stuur_betaling_herinnering(self):
        for factuur_open in self.facturen_open:
            if self.facturen_open: 
                factuur_open.status = Factuur_Status.EERSTE_HERINNERING
                print(f'Betaal je factuur: {factuur_open}')

        for facturen in self.facturen:
            if facturen.status == Factuur_Status.EERSTE_HERINNERING:
                facturen.status = Factuur_Status.TWEEDE_HERINNERING
                print(f'Dit is je tweede herinnering. Betaal je factuur: {facturen}')

        for facturen in self.facturen:
            if facturen.status == Factuur_Status.TWEEDE_HERINNERING:
                facturen.status = Factuur_Status.OVERGEDRAGEN_AAN_INCASSO
                print(f'Je factuur is overgedragen aan de incassobureau.')
                
# Blokkeert actieve klanten die een factuur hebben die naar incasso is gegaan   
    def blokkeer_klanten(self):
        for order in self.orders:
            for klant in self.klanten:
                if klant.klant_id == order.klant_id and klant.status == Klant_Status.ACTIEF:
                    for factuur in self.facturen:
                        if factuur.factuur_id == order.factuur_id and factuur.status == Factuur_Status.OVERGEDRAGEN_AAN_INCASSO:
                            klant.status = Klant_Status.GEBLOKKEERD
                            print(f'Klant {klant.bedrijfsnaam} is geblokkeerd vanwege factuur {factuur.factuur_id}.')


# Voorbeelddata
f1 = Factuur(5, '26-05-2026', 350, '29-06-2026', Factuur_Status.OPEN)
f2 = Factuur(8, '22-05-2026', 170, '29-06-2026', Factuur_Status.BETAALD)
f3 = Factuur(9, '26-01-2025', 400, '29-06-2026', Factuur_Status.OVERGEDRAGEN_AAN_INCASSO)

facturen = [f1, f2, f3]


#LIJST MET KLANTEN. In de lijst wil ik alle actieve klanten > die factuurstatus = incasso hebben blokkeren
k1 = Klant(4, 'Apotheek Tom', 2500, 15, Klant_Status.ACTIEF, 4)
k2 = Klant(5, 'Apotheek Salman', 1700, 5, Klant_Status.ACTIEF, 6)
k3 = Klant(7, 'Apotheek Ali', 2000, 10, Klant_Status.GEBLOKKEERD, 7)

klanten = [k1, k2, k3]

o1 = Order(1, 350, k1.klant_id, f1.factuur_id)
o2 = Order(2, 400, k2.klant_id, f3.factuur_id) # deze koppeling moet klant blokkeren
o3 = Order(3, 170, k3.klant_id, f2.factuur_id)

orders = [o1, o2, o3]

administratie = Administratie_service(facturen, klanten, orders)
administratie.controleer_open_facturen()
administratie.stuur_betaling_herinnering()
administratie.blokkeer_klanten()
