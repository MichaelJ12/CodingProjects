from datetime import date
from aquisitie import (
    Adres,
    Contactpersoon,
    Klant,
    Klant_Status,
    Order,
    Acquisitie_service,
)


def main():
    a1 = Adres(1, "Kerkstraat", "10", "Amsterdam", "1011AA")
    a2 = Adres(2, "Langeweg", "5", "Utrecht", "3511BB")

    c1 = Contactpersoon(1, "info@bedrijf.nl", "0612345678", "Jan", "Jansen")

    klanten = [
        Klant(1, "Bedrijf BV", 120000, 0.0, Klant_Status.potentieel, a1.adres_id, c1.contactpersoon_id, a2.adres_id),
        Klant(2, "Andere BV", 90000, 0.0, Klant_Status.potentieel, a1.adres_id, c1.contactpersoon_id, a2.adres_id),
        Klant(3, "Actief BV", 300000, 0.0, Klant_Status.actief, a1.adres_id, c1.contactpersoon_id, a2.adres_id),
    ]

    orders = [
        Order(101, klant_id=1, bedrag=5000.0, orderdatum=date(2026, 1, 10)),
        Order(102, klant_id=3, bedrag=12000.0, orderdatum=date(2026, 1, 12)),
    ]

    acquisitie = Acquisitie_service(klanten, orders)

    for k in acquisitie.check_potentiele_klant():
        print(k.bedrijfsnaam, acquisitie.bied_incentive_aan(k))


if __name__ == "__main__":
    main()


