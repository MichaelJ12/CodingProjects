import random

# Start van het programma
print("hi welkom")

# Vraag naam van de gebruiker
naam = input("wat is je naam: ")

# Vraag een getal tussen 5 t/m 10
getal = input("kies een getal tussen 5 en 10: ")

print(f"OK {naam}, jij hebt gekozen voor: {getal} ")

# Bevestiging vragen
answer = input("is dit juist (j/n): ")

# Vraag om een nieuw getal in gedachten te nemen
if answer == "j":
   nieuwe_getal = int(input(f"neem nu een nieuwe getal in je hoofd tussen 0 en {getal}: "))
else:
    nieuwe_getal = int(input(f"We gaan toch beginnen. Neem een nieuw getal in je hoofd tussen 0 en {getal}: "))

# Start getal dat de computer raadt
random_start_num = random.randint(1, 10)

# Lijst om alle gokken bij te houden
gokken = []
count = 1        # Aantal keren dat er gegokt is
even_count = 0   # Aantal keren dat een even getal is gegokt

# Eerste gok tonen
print(f"Is het soms: {random_start_num}?")

# Antwoord vragen
answer = input("is dit juist (j/n): ")

# Voeg gok toe aan lijst
gokken.append(random_start_num)
juist_getal = gokken[-1]   # Houd bij wat de laatste gok was

# Zolang het antwoord 'n' is, blijft hij raden
while answer == "n":
   random_num = random.randint(1, 10)  # Nieuwe gok
   gokken.append(random_num)           # Voeg gok toe aan de lijst
   juist_getal = gokken[-1]            # Update laatste gok
   count += 1                          # Tel er 1 bij op
   answer = input(f"Oh ehhh… is het dan: {random_num}? ")

   # Check of het een even getal i
   if random_num % 2 == 0:
       even_count += 1
   if random_start_num % 2 == 0:
       even_count += 1
    
       
   # Als het juist is, stop en toon resultaat
   if answer == "j":
        print(f"Niet slecht, in {count} keer geraden!")

# Eindresultaat tonen
print(
    f"Ik heb het volgende gegokt: {'-'.join(str(g) for g in gokken)}. "
    f"En het was {juist_getal}! "
    f"Ik heb {even_count} keer een even getal gegokt."
)

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

# ff nog een test
