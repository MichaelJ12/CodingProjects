import random
  
# Ask the user for their name and ensure it only contains letters
while True:
    name: str = input("hallo, wat is jouw naam? ")
    if name.isalpha():  # checks if all characters are letters
        break
    else:
        print("voer letters in!")

# Ask the user for their age and ensure it is a valid integer
while True:
    try: 
        age: int = int(input(f"Oke {name} hoe oud ben jij? "))
        if type(age) == int:  # redundant but ensures the input is int
            break
    except ValueError:
        print("voer een nummer in!")

# Calculate birth year and a "changed" birth year for guessing game
birth_date: int = 2025 - age 
changed_birth_date: int = birth_date - 1

print(f"Welkom {name}, jij bent waarschijnlijk in {birth_date} geboren.")

# Function to ensure the user input is always 'j' or 'n'
dot = "."  # used to show suspense in repeated guesses
guess = 0

def ask():
    while True:
        answer = input("is dit juist (j/n): ").lower()
        if answer in ("j", "n"):
            return answer
        print("vul (j/n) in")

# Start the guessing game for birth year
answer = ask()
if answer == "j":
    print("Goed van mij he?!")
else:
    guess += 1
    print(f"Ah, sorry {name}, dat moet natuurlijk dan {changed_birth_date} zijn.")

    while True:
        answer = ask()
        if answer == "j":
            print(f"Niet slecht, in {guess} keer geraden!")
            break

        # Generate new guesses with some suspense
        guess += 1
        new_birth_date = changed_birth_date - (guess - 1)
        print(f"Oh ehhh{dot} is het dan {new_birth_date}?")
        dot += "."

print("_" * 40)

# Ask the user for their full name and split it into first and last name
while True:
    try:
        full_name: str = input("wat is jouw volledige naam?: ")
        while True:
            if type(full_name) == str:
                break
            else:
                print("voer letters in!")

        split_full_name = full_name.split()
        first_name = split_full_name[0]
        last_name = split_full_name[-1]
        if len(split_full_name) <= 1:  # ensures at least first and last name
            print("vul jouw volledige naam in!")
        else:
            break
    except IndexError:
        print("vul jouw volledige naam in!")

# Fun output: reverse the last name to create a "fantasy" name
print(f"Hoi {first_name}, een leuke fantasienaam voor jou is {last_name[::-1]}.")

# List of colors
color = [
    "rood",
    "blauw",
    "groen",
    "geel",
    "oranje",
    "paars",
    "roze",
    "bruin",
    "grijs",
    "turquoise"
]

print("_" * 40)

# Ask the user for a number between 1 and 10 to pick a color from the list
while True:
    try:
        num = int(input("Voer een getal in tussen 1-10: "))
        if 1 <= num < 11:
            break
        else:
            print("Het getal moet tussen 1 en 10 liggen.")
    except ValueError:
        print("Voer een geldig getal in.")

# Pick the color based on user input
chosen_color = color[num-1]  # -1 because list index starts at 0
print(f"Verrassing {first_name}! De {num}e kleur is {chosen_color}! Mooi he?")

# Function to generate a dictionary of random colors with random "worth" values
def make_dict(num):
    chosen_color = random.sample(color, num)  # pick num random colors

    mine_dict = {}
    for colors in chosen_color:
        # Generate a random float with 1 decimal
        worth = round(random.uniform(0, 10), 1)
        # Replace dot with comma for display
        worth_str = str(worth).replace(".", ",")
        # Add to dictionary
        mine_dict[colors] = worth_str
    return mine_dict            

# Generate and display the dictionary
result = make_dict(num)
print(result)
