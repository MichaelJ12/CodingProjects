
class Order:
    def __init__(self, totaalbedrag: float):
        self.totaalbedrag = totaalbedrag

    def __str__(self) -> str:
        return f"Totaalbedrag: {self.totaalbedrag} |"

class Klant:
    def __init__(self, jaaromzet: float):
        self.jaaromzet = jaaromzet

    def __str__(self) -> str:
        return f"Jaaromzet: {self.jaaromzet} |"
    

# verkoop proces with functions that will create a order or klant and calculate discounts

class Verkoop_Proces:       
    def bereken_bedrag_korting(self, order: Order) -> float:
        bedrag = order.totaalbedrag

        # returns discounted amount based on order total

        if bedrag >= 500:
            return bedrag * 0.95 
        else:
            return bedrag 

    def bereken_klant_korting(self, klant: Klant) -> float:
        
        # returns discounted amount based on jaaromzet

        if klant.jaaromzet < 10_000:
            return 0.05
        elif klant.jaaromzet < 20_000:
            return 0.10
        else:
            return 0.15
