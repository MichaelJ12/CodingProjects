from spaceship import Spaceship, Fleet, planets

def test_send_ship_sets_destination():
    fleet = Fleet(planets)
    ship = Spaceship('ss-Test')
    fleet.add_ship(ship)

    fleet.send_ship(ship, "Mercurius")

    assert ship.destination == "Mercurius"
    assert len(fleet.flight_log) == 1 

    
def test_Flying_ship_cant_be_send_again():
    fleet = Fleet(planets)
    ship = Spaceship('ss-Test')
    fleet.add_ship(ship)

    fleet.send_ship(ship, "Mercurius")

    fleet.send_ship(ship, "Venus")

    assert ship.destination == "Mercurius"
    assert len(fleet.flight_log) == 1 