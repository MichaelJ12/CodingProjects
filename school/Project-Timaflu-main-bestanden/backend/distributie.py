from enum import Enum


class Levering_Status(Enum):
    GEPLAND = "gepland"
    AFGELEVERD = "afgeleverd"
    KLANT_NIET_AANWEZIG = "klant_niet_aanwezig"
    RETOUR_MAGAZIJN = "retour_magazijn"


class Medewerker:
    def __init__(self, medewerker_id, naam, rol):
        self.medewerker_id = medewerker_id
        self.naam = naam
        self.rol = rol


class Order:
    def __init__(self, order_id):
        self.order_id = order_id


class Levering:
    def __init__(self, levering_id, order, koerier):
        self.levering_id = levering_id
        self.order = order
        self.koerier = koerier
        self.status = Levering_Status.GEPLAND
        self.afleverpogingen = 0


class Distributie_Proces:

    def klant_niet_aanwezig(self, levering):

        levering.afleverpogingen += 1
        print(f"Afleverpoging {levering.afleverpogingen} door koerier {levering.koerier.naam}")

        if levering.afleverpogingen == 1:
            levering.status = Levering_Status.KLANT_NIET_AANWEZIG
            print("Klant niet aanwezig bij eerste poging.")
            print("Koerier belt de klant.")
            print("Bestelling wordt later op de dag opnieuw aangeboden.")
        else:
            levering.status = Levering_Status.RETOUR_MAGAZIJN
            print("Klant niet aanwezig bij tweede poging.")
            print("Bestelling gaat terug naar het magazijn.")
            print("Verkoop wordt geïnformeerd.")
            print("Verkoop neemt contact op met de klant voor een nieuwe afspraak.")
            print("Extra kosten worden geregistreerd.")

        print(f"Status gewijzigd naar: {levering.status.value}")

    def levering_afgerond(self, levering):

        levering.status = Levering_Status.AFGELEVERD
        print("Bestelling is afgeleverd.")
        print("Klant heeft getekend voor ontvangst.")
        print(f"Status gewijzigd naar: {levering.status.value}")


# Test
if __name__ == "__main__":
    order = Order(1001)
    koerier = Medewerker(1, "Jan", "koerier")
    levering = Levering(1, order, koerier)

    proces = Distributie_Proces()

    proces.klant_niet_aanwezig(levering)
    proces.klant_niet_aanwezig(levering)
