planets = {
    "Mercurius": ("maan1", "maan2"),
    "Venus": ("maan1", "maan2"),
    "Aarde": ("maan1", "maan2"),
    "Mars": ("maan1", "maan2"),
    "Jupiter": ("maan1", "maan2"),
    "Saturnus": ("maan1", "maan2"),
    "Uranus": ("maan1", "maan2"),
    "Neptunu": ("maan1", "maan2")
}

class Fleet(object):
    def __init__(self, locations) -> None:
        self.ships = []
        self.locations = locations
        self.flight_log = []
    
    def add_ship(self, ship) -> None:
        self.ships.append(ship)
        print(f"ship: {ship.name} added to fleet")
        print(f"Fleet now has: {[ship.name for ship in self.ships]}")
        
    def send_ship(self, ship, planet, moon=None) -> None:
        if ship.current_location == ship.destination or ship.current_location is None:

            if planet in self.locations:

                if moon is None:
                    ship.destination = planet
                    print(f"ship: {ship.name} is flying to: {ship.destination}")
                    self.flight_log.append({
                        "ship": ship.name,
                        "from": ship.current_location,
                        "to": ship.destination
                    })
                elif moon in self.locations[planet]:
                    ship.destination = (planet, moon)
                    print(f"ship: {ship.name} is flying to: {moon} van {planet}")
                    self.flight_log.append({
                        "ship": ship.name,
                        "from": ship.current_location,
                        "to": ship.destination
                    })
                else:
                    print(f"{moon} is not a valid moon of {planet}")
            
            else:
                print("vul een geldige planeet in ")
                print(f"planeten: {list(self.locations.keys())}")

    def ship_arrived(self, ship) -> None:
        ship.current_location = ship.destination
        print(f"ship: {ship.name} arrived at: {ship.destination}")


    def status(self):
        fleet = self.ships
        print(f"fleet status:")
        for ship in fleet:
            ship.print()

    def print_flight_log(self):
        print("Flight log:")
        for flight in self.flight_log:
            print(f"    {flight['ship']}: from {flight['from']} -> {flight['to']}")

    def send_free_ship(self, planet, moon=None) -> None:
        for ship in self.ships:
            if ship.destination == None:

                if planet in self.locations:

                    if moon is None:
                        ship.destination = planet
                        print(f"ship: {ship.name} is flying to: {ship.destination}")
                        self.flight_log.append({
                        "ship": ship.name,
                        "from": ship.current_location,
                        "to": ship.destination
                        })
                        break
                    elif moon in self.locations[planet]:
                        ship.destination = (planet, moon)
                        print(f"ship: {ship.name} is flying to: {moon} van {planet}")
                        self.flight_log.append({
                        "ship": ship.name,
                        "from": ship.current_location,
                        "to": ship.destination
                        })
                        break
                    else:
                        print(f"{moon} is not a valid moon of {planet}")
                
                else:
                    print("vul een geldige planeet in ")
                    print(f"planeten: {list(self.locations.keys())}")

    def check_locations(self):
        return self.locations

class Spaceship(object):
    def __init__(self, name):
        self.name = name 
        self.current_location = None
        self.destination = None

    def print(self) -> None:
        print(f"  {self.name}: current_location={self.current_location}, destination={self.destination}")



if __name__ == '__main__':
    s = Spaceship('SS-Aplha')
    print(s.print())   
    v = Spaceship('SS-Vanguard')
    print(v.print()) 
    e = Spaceship('SS-Explorer')
    print(e.print()) 
    a = Spaceship('SS-Aurora')
    print(a.print()) 
    o = Spaceship('SS-Obsidian')
    print(o.print()) 
    n = Spaceship('SS-Nova')
    print(n.print()) 
    p = Spaceship('SS-Phoenix')
    print(p.print()) 
    r = Spaceship('SS-Orion')
    print(r.print()) 

    print("-" * 40)

    f = Fleet(planets)

    f.add_ship(s)
    f.add_ship(v)
    f.add_ship(e)
    f.add_ship(a)
    f.add_ship(o)
    f.add_ship(n)
    f.add_ship(p)
    f.add_ship(r)

    print("-" * 41)

    f.send_ship(s,'Mercurius')
    f.send_ship(v,'Venus', 'maan1')
    print()
    f.send_free_ship('Uranus')
    f.send_free_ship('Neptunu', 'maan2')
    print("-" * 40) 
    f.print_flight_log()
    print("-" * 40) 

    f.ship_arrived(s)

    print("-" * 40) 
    f.send_ship(s,'Jupiter')  

    f.print_flight_log()

    f.status()



    
   


