users: list = ['dave', 'bob', 'aels', 'tim', 'diana', 'raiven'] 

service = [
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

def print_service(service: list):
    for index in service:
        print(f"{index['date']} - {index['name']} ({index['time']})")
        for rol in index['roles']:
            if user == rol['person']:
                print(f"{rol['role_name']}:  *{rol['person']}*")
            else: 
                print(f"{rol['role_name']}: {rol['person']}")
        print('-' * 50)


print("Kerkdienst planner - versie 0.1")
print("-" * 50)
print("Lijst met werkers:")

for i, u in enumerate(users, start=1):
    print(f"{i}. {u}")
current_user = int(input(f"kies een werker: "))

user = users[current_user-1]

print(f"welkom {user}")
print("-" * 50)
print_service(service)