from tampering_product import Product, MyType


def main():
    # make list for the products
    products = []

    # make a set product and add it to the list products
    p = Product("Tomatensoep", MyType.CAN, 250)
    products.append(p)

    # loop the user input till 'x' is answerd
    while True:
        name = input("voer naam in: ")

        # makes sure that the user_input access the enum value
        user_input_int = int(input(f"voer tpye in (1 = Blikje, 2 = Doos, 3 = Fles): "))
        user_input_enum = MyType(user_input_int)

        contents = int(input("voer inhoud in: "))

        # make a product with the stored user inputs and add it to the list
        product = Product(name, user_input_enum, contents)
        products.append(product)

        # stop if x is tpyed
        stop = input("Type het karakter 'x' als u klaar bent: ").lower()
        if stop == 'x':
            break

    # loop through the list for the amount that is in the list and show per product the info    
    for product in products:
        product.show_prodcut_info()


if __name__ == '__main__':
    main()