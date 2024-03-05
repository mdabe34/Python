nato_alphabet = {
    "a": "alpha", "b": "bravo", "c": "charlie", "d": "delta", "e": "echo",
    "f": "foxtrot", "g": "golf", "h": "hotel", "i": "india", "j": "juliet",
    "k": "kilo", "l": "lima", "m": "mike", "n": "november", "o": "oscar",
    "p": "papa", "q": "quebec", "r": "romeo", "s": "sierra", "t": "tango",
    "u": "uniform", "v": "victor", "w": "whiskey", "x": "x-ray", "y": "yankee",
    "z": "zulu"
}

def spell_word(word):

    for char in word.lower():
        if char in nato_alphabet:
            print(nato_alphabet[char], end=" ")
        else:
            print(char, end=" ")

def main():
    while True:
        word = input("Enter a word (or 'q' to quit): ").lower()
        if word == 'q':
            break
        spell_word(word)
        print()  


if __name__ == "__main__":
    main()