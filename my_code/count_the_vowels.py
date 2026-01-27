def count_vowels(word:str)-> tuple[int, list]:
    vowels_check: set = {"a", "e", "i", "o", "u"}
    count: int = 0
    vowels: list = []
    

    for letter in word:
        if letter.lower() in vowels_check:
            vowels.append(letter)
            count += 1 

    return count, vowels
            
word: str = "indices"

count, vowels = count_vowels(word)
print(f"this word has {count} vowels: {vowels}")


