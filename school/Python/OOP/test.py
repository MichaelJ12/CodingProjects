class GameObject(object):
    def __init__(self, posistion: list, name: str, health: int) -> None:
        self.posistion = posistion
        self.name = name
        self.heath = health
        
    def show_data(self):
        return self.posistion
    
    def take_dmg(self, amount: int):
        pass
    
    def is_terminated(self, bool: bool):
        pass
        



if __name__ == '__main__':
    gb = GameObject([10,10], 'dave', 100)
    
    
    print(gb.show_data())