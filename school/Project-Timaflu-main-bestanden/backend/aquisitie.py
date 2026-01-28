from enum import Enum
from datetime import date


class Klant_Status(Enum):
    potentieel = "potentieel"
    actief = "actief"
    geblokkeerd = "geblokkeerd"


class Adres:
    def __init__(self, adres_id, straat, huisnummer, plaats, postcode):
        self.adres_id = adres_id
        self.straat = straat
        self.huisnummer = huisnummer
        self.plaats = plaats
        self.postcode = postcode


class Contactpersoon:
    def __init__(self, contactpersoon_id, email, telefoon, voornaam, achternaam):
        self.contactpersoon_id = contactpersoon_id
        self.email = email
        self.telefoon = telefoon
        self.voornaam = voornaam
        self.achternaam = achternaam


class Klant:
    def __init__(
        self,
        klant_id,
        bedrijfsnaam,
        jaaromzet,
        korting,
        status,
        hoofd_adres_id,
        contactpersoon_id,
        factuur_adres_id,
    ):
        self.klant_id = klant_id
        self.bedrijfsnaam = bedrijfsnaam
        self.jaaromzet = jaaromzet
        self.korting = korting
        self.status = status
        self.hoofd_adres_id = hoofd_adres_id
        self.contactpersoon_id = contactpersoon_id
        self.factuur_adres_id = factuur_adres_id


class Order:
    def __init__(self, order_id, klant_id, bedrag, orderdatum: date):
        self.order_id = order_id
        self.klant_id = klant_id
        self.bedrag = bedrag
        self.orderdatum = orderdatum


class Acquisitie_service:
    def __init__(self, klanten, orders):
        self.klanten = klanten
        self.orders = orders

    def check_potentiele_klant(self):
        klant_ids_met_order = {o.klant_id for o in self.orders}
        return [
            k
            for k in self.klanten
            if k.status == Klant_Status.potentieel
            and k.klant_id not in klant_ids_met_order
        ]

    def bied_incentive_aan(self, klant: Klant):
        klant_ids_met_order = {o.klant_id for o in self.orders}

        if klant.status == Klant_Status.potentieel and klant.klant_id not in klant_ids_met_order:
            klant.korting = 10
            return 10

        return 0
