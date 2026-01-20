from sad_product import SmartAccessDevice, MyType

def main():
    sads = []

    c = SmartAccessDevice('ingang', 2, MyType.ENTRANCE)
    sads.append(c)

    while True:
        user_input_id = input("Voer id SAD in: ")


        user_input_type = int(input("Voer type in (1 = Ingang, 2 = uitgang, 3= beide): "))
        type = MyType(user_input_type)

        user_input_standaard = int(input("Voer standaard 'open tijd' in: "))


        sad = SmartAccessDevice(user_input_id, user_input_standaard, type)
        sads.append(sad)

        stop = input("typ het karakter 'x' als u klaar bent: ").lower()

        if stop == 'x':
            break

    for sad in sads:
        sad.show_sad_info()











if __name__ == '__main__':
    main()