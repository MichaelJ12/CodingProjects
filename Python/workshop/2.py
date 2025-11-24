class Rekening(object):
    def __init__(self, saldo) -> None:
        self.set_saldo(saldo)

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo


if __name__ == '__main__':
    R = Rekening(50)

    print(R.get_saldo())

    R.set_saldo(100)

    print(R.get_saldo())