from administratie import (Factuur,Klant,Order,Administratie_service,Factuur_Status,Klant_Status)


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
