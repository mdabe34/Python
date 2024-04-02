def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]

    def modify_artist():
        while True:
            try:
                index = int(input("Enter the index of the artist to replace: "))
                if 0 <= index < len(top_artists):
                    new_artist = input("Enter the new artist name: ")
                    top_artists[index] = new_artist
                    print("Updated list:", top_artists)
                    break 
                else:
                    print("Index out of range. Please try again.")
            except (ValueError, IndexError):
                print("An input error occurred.")

    modify_artist() 

main()