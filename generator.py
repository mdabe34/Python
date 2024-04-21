def two_letter_combinations(characters):

    for i in range(len(characters)):
        for j in range(len(characters)):
            yield characters[i] + characters[j]

def main():
  
    characters = ['p', 'o', 'e', 'm', 's']  
    for combination in two_letter_combinations(characters):
        print(combination)

if __name__ == "__main__":
    main()