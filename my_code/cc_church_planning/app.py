users: list = ['dave', 'bob', 'aels', 'tim', 'diana', 'raiven'] 

unavailable = {}

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

def print_service(service: list):
    for index in service:
        print(f"{index['date']} - {index['name']} ({index['time']})")
        for rol in index['roles']:
            if user == rol['person']:
                print(f"{rol['role_name']}:  *{rol['person']}*")
            else: 
                print(f"{rol['role_name']}: {rol['person']}")
        print('-' * 50)

print(unavailable)
print("Kerkdienst planner - versie 0.1")
print("-" * 50)
print("Lijst met werkers:")

for i, u in enumerate(users, start=1):
    print(f"{i}. {u}")
user = int(input(f"kies een werker: "))

current_user = users[user-1]

print(f"welkom {user}")
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
print("-" * 50)
# print_service(service)