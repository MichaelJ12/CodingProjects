from inkoop_proces import Product, Product_Leverancier, Inkoop_Proces, Voorraad_status, Leverbaarheid_Status

def main():

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
if __name__ == '__main__':
    main()


        

    