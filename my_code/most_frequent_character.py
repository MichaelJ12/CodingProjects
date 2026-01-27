def most_frequent_char(word: str) -> tuple[int, str]:
    char: dict = {}
    highest_count:int = 0
    highest_count_letter:str = ""

    for letter in word:
        letter = letter.lower()
        if not letter.isalpha():
             continue

        if letter in char:
            char[letter] += 1 
        else:
            char[letter] = 1
            
        if  highest_count < char[letter]:
                highest_count = char[letter] 
                highest_count_letter = letter

    return highest_count, highest_count_letter   

word: str = "backward"
count, letter = most_frequent_char(word)
print(f"The most frequent letter is '{letter}' with {count} occurrences")