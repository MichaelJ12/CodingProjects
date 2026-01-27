class Knight(object):
    def __init__(self, name, lvl=5, weapon='sword'):
        self.name = name
        self.lvl = lvl
        self.weapon = weapon

    def __str__(self):
        return f"Knight {self.name}: level {self.lvl}, weapon: {self.weapon}"

    def __eq__(self, other):
        if self.name == other.name and self.lvl == other.lvl and self.weapon == other.weapon:
            return True
        else:
            return False 
        
    def level_up(self):
        self.lvl += 1
        return self.lvl

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
    
    def attack(self):
        print(f"{self.name} attacks with {self.weapon}")

    def describe(self):
        print(f"knight {self.name}: level {self.lvl}, weapon: {self.weapon}")
        

diana = Knight("Diana", 5, "Energy Whip")
diana.attack()
diana.level_up()
print(diana.lvl)
diana.change_weapon("sword")
diana.attack()
diana.describe()
print(diana)

d1 = Knight("Diana", 6, "Sword")
d2 = Knight("Diana", 6, "Sword")

bob = Knight("bob", 2,"sword")

print(bob)

bob.attack()
