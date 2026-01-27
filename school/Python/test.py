import random

# Start van het programma
print("hi welkom")

# Vraag naam van de gebruiker
naam: str = str(input("wat is je naam: "))

def check_int(user_input) -> bool:
    try:
        user_input = int(user_input)
        return True
    except ValueError:
        return False
    
# Vraag een getal tussen 5 t/m 10
while True:
    try:
        user_input = input("kies een getal tussen 5 en 10: ")
        number = int(user_input)
        if number <= 5 or number >= 10:
            print("nummer mag niet lager dan 5 of hoger dan 10")
        else:
            break
    except ValueError:
        print("Voer een geldig getal in (een integer).")

print(f"OK {naam}, jij hebt gekozen voor: {number} ")

answer_options: tuple = ("j", "n")

# Bevestiging vragen
answer = str(input("is dit juist (j/n): "))
    
# Vraag om een nieuw getal in gedachten te nemen
while True:
    if answer in answer_options:
        break      
    else:
        print("vul (j/n) in")
        answer = str(input("is dit juist (j/n): ")) 
        continue
while True:
    if answer == "j":
        user_input = input(f"neem nu een nieuwe getal in je hoofd tussen 0 en {number}: ")
        if check_int(user_input):
            break
        else:
            print("Voer een geldig getal in (een integer).")
    else:
        user_input = input(f"We gaan toch beginnen. Neem een nieuw getal in je hoofd tussen 0 en {number}: ")
        if check_int(user_input):
            break
        else:
            print("Voer een geldig getal in (een integer).")


list_numbers: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_choice: int = random.choice(list_numbers)
random_start_num: int = random_choice

# functie om de nummer die geraden is uit de list te halen
def del_list_num(random_start_num) -> None:
    if random_start_num == random_start_num:
        list_numbers.remove(random_start_num)

# Lijst om alle gokken bij te houden
guesses: list = []
 
count:int = 0       # Aantal keren dat er gegokt is
even_count: int = 0   # Aantal keren dat een even getal is gegokt

new_answer = "n"

# Eerste gok tonen
while new_answer == "n":
    random_choice: int = random.choice(list_numbers)
    random_start_num: int = random_choice

    print(f"Is het soms: {random_start_num}? ")
    new_answer: str = str(input("is dit juist (j/n): "))

    del_list_num(random_start_num)  

    guesses.append(random_start_num)
    
    count += 1

    if random_start_num % 2 == 0:
        even_count += 1
else:
    juist_getal = guesses[-1]  
    print(f"Niet slecht, in {count} keer geraden!"
          f"Ik heb het volgende gegokt: {'-'.join(str(g) for g in guesses)}. "
          f"En het was {juist_getal}! "
          f"Ik heb {even_count} keer een even getal gegokt.")

# Lijst met namen
namen = ["Lucas", "Emma", "Saar", "Milan", "Noah", "Lotte", "Finn", "Tess", 
         "Sam", "Liam", "Eva", "Jesse", "Nina", "Max", "Anna", "Daan", "Bo", 
         "Levi", "Fien", "Olaf"]

# Functie die een dictionary maakt met omgekeerde namen
def maak_omgekeerde_dict(getal):
    # Kies 'getal' unieke namen willekeurig uit de lijst
    gekozen_namen = random.sample(namen, getal)
    
    # Maak dictionary waarbij de naam de key is en de omgekeerde naam de value
    omgekeerde_dict = {naam: naam[::-1] for naam in gekozen_namen}
    
    return omgekeerde_dict

# Vraag de gebruiker om invoer (een getal onder de 20)
while True:
    try:
        getal = int(input("Voer een getal in onder de 20: "))
        if 0 <= getal < 20:
            break
        else:
            print("Het getal moet tussen 0 en 19 liggen.")
    except ValueError:
        print("Voer een geldig getal in.")

# Verrassingstekst: pak de naam op de (getal-1) positie in de lijst
gekozen_naam = namen[getal-1]  # -1 omdat lijsten bij 0 beginnen
print(f"Verrassing! {naam}, de {getal}e naam is {gekozen_naam}!!")

# Maak de dictionary en toon hem
resultaat = maak_omgekeerde_dict(getal)
print("De dictionary is:", resultaat)
  

