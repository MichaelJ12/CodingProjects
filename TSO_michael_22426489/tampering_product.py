from enum import Enum

class MyType(Enum):
    CAN = 1
    BOX = 2
    BOTTLE = 3

class Product(object):

    def __init__(self, name, type: MyType, real_contents) -> None:
        self.name = name
        self.real_contents = real_contents
        self.set_type(type)

    def set_type(self, type):
        self.type = type
        if self.type == MyType.CAN and self.real_contents > 10:
            self.type = MyType.BOTTLE


    def get_type(self):
        return self.type

    def get_contents(self) -> int:
        return self.real_contents * 1.1
    
    def show_prodcut_info(self):
        contents = self.get_contents()
        if self.type == MyType.BOTTLE:
            print(f"product: {self.name}, inhoud: {contents}")
            print(f"    - (Dit is een fles)")
        else:
            print(f"products: {self.name}, inhoud: {contents}")


if __name__ == "__main__":
    p = Product('cheese', MyType.CAN, 1000)
    print(p.get_contents())

    p.show_prodcut_info()

    print(p.get_type())

    p.set_type(MyType.CAN)

    print(p.get_type())

    p.show_prodcut_info()


    b = Product('cheese', MyType.CAN, 1000)
    print(b.get_type())

    