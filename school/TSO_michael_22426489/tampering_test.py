from tampering_product import Product, MyType

def test_tampering():
    p = Product('cheese', MyType.CAN, 1000)

    assert  p.real_contents * 1.1 == p.get_contents()


def test_upgrade_to_bottle():
    a = Product('cola', MyType.CAN, 100)
    a.get_type()

    assert  a.get_type() == MyType.BOTTLE
