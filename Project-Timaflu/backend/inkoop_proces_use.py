from inkoop_proces import Product, Product_Leverancier, Inkoop_Proces, Voorraad_status, Leverbaarheid_Status

def main():

    p1 = Product(1, "Paracetamol", 2.55, 100, 250, Voorraad_status.OP_VOORRAAD)
    p2 = Product(2, "Ibuprofen", 3.10, 80, 60, Voorraad_status.ONDER_MINIMUM)
    p3 = Product(3, "Amoxicilline", 12.99, 50, 0, Voorraad_status.NIET_OP_VOORRAAD)
    p4 = Product(4, "Aspirine", 2.80, 120, 130, Voorraad_status.OP_VOORRAAD)
    p5 = Product(5, "Insuline", 45.00, 30, 10, Voorraad_status.ONDER_MINIMUM)

    pl1 = Product_Leverancier("Paracetamol", "PharmaSupply BV", 1.80, Leverbaarheid_Status.LEVERBAAR)
    pl2 = Product_Leverancier("Insuline", "MedicoGroothandel", 5.40, Leverbaarheid_Status.LEVERBAAR)
    pl3 = Product_Leverancier("Ibuprofen", "HealthCore NV", 2.10, Leverbaarheid_Status.NIET_LEVERBAAR)
    pl4 = Product_Leverancier("Aspirine", "CheapMeds", 1.95, Leverbaarheid_Status.LEVERBAAR)
    pl5 = Product_Leverancier("Amoxicilline", "BioPharm", 10.50, Leverbaarheid_Status.NIET_LEVERBAAR)

    producten = [p1,p2,p3,p4,p5]
    leveranciers = [pl1,pl2,pl3,pl4,pl5]

    inkoop = Inkoop_Proces(producten, leveranciers) 


  
    inkoop.controleer_voorraad()

if __name__ == '__main__':
    main()


        

    