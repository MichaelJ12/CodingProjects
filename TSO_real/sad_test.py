from sad_product import SmartAccessDevice, MyType

def test_entrance():
    a = SmartAccessDevice('ingang', 3, MyType.BOTH)

    assert a.get_type()

def test_actual_open_time():
    b = SmartAccessDevice('ingang23', 10, MyType.BOTH)

    assert b.get_actual_open_time(99)
    