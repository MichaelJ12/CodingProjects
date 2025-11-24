class Persoon(object):
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def get_msg(self):
        print(f"hallo {self.naam} jij bent {self.leeftijd}")





if __name__ == "__main__":
    p = Persoon("bob", 12)

    p.get_msg()


