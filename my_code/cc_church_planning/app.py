users: list = ['dave', 'bob', 'jan', 'tim', 'diana', 'raiven'] 

unavailable = {
    'dave' : ['01-02-2026']
}

service: list = [
    {
        "name" : "Sunday celabration!",
        "date" : "01-02-2026",
        'time' : '11:00',
        'roles' : [
            {'role_name' : 'livestream', 'person' : 'dave'},
            {'role_name' : 'camera', 'person' : 'raiven'}
        ]
    },
    {
        "name" : "bijbelstudie!",
        "date" : "30-01-2026",
        'time' : '19:30',
        'roles' : [
            {'role_name' : 'livestream', 'person' : 'bob'},
            {'role_name' : 'camera', 'person' : 'aels'}
        ]
    }
]

def create_service():
    while True:
        answer = str(input('Maak een service aan? (j/n): ')).lower()
        if answer == 'j':
            name = str(input("Geef de service een naam: "))
            date = input("geef het een datum: ")
            time = input("en een tijd: ")
                     
            service = {
                'name' : name,
                'date' : date,
                'time' : time,
                # add roles to service
                'roles' : []
            }

            services.append(service)
            print(services)
            
        elif answer == 'n':
            print(services)
            break    

def print_service():
    for index in services:
        print(f"{index['date']} - {index['name']} ({index['time']})")
        for rol in index['roles']:
            if rol['person'] in unavailable and index['date'] in unavailable[rol['person']]:
                print(f"{rol['role_name']}:  {rol['person']} = (ONBESCHIKBAAR)")
            elif current_user == rol['person']:
                print(f"{rol['role_name']}:  *{rol['person']}*")
            else:
                print(f"{rol['role_name']}: {rol['person']}")
        print('-' * 50)

def set_unavailable():
    while True:
        print(unavailable)
        answer = input('Wil je een vakantiedag toevoegen? (j/n): ').lower()
        if answer == 'j':
            date = input("type datum: ")
            if current_user not in unavailable:
                unavailable[current_user] = []
                unavailable[current_user].append(date)
            else:
                unavailable[current_user].append(date)
            
        elif answer == 'n':
            break        
    print(unavailable)

    

print("Kerkdienst planner - versie 0.1")

create_service()

print("-" * 50)
print("Lijst met werkers:")

for i, u in enumerate(users, start=1):
    print(f"{i}. {u}")

user = int(input(f"kies een werker: "))
current_user = users[user-1]

print(f"welkom {current_user}")

set_unavailable()

print("-" * 50)

print_service()