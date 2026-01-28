import verkoop_proces

# creating order and klant instances

order = verkoop_proces.Order(750)
klant = verkoop_proces.Klant(15000)

service = verkoop_proces.Verkoop_Proces()

# calculating final amount after applying discounts

bedrag_na_korting = service.bereken_bedrag_korting(order)
klant_korting = service.bereken_klant_korting(klant)

eindbedrag = bedrag_na_korting * (1 - klant_korting)

print(f"Eindbedrag: {eindbedrag}")
