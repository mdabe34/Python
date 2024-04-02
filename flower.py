def main():
    flowerList = []
    while True:
        flowerName = input("Enter a flower name (type 'done' when finished): ")
        if flowerName.lower() == "done":
            break
        flowerList.append(flowerName)

    flowerList.sort()
    print("\nYour sorted flower list:")
    for i, flower in enumerate(flowerList):
        print(f"{i + 1}. {flower}")

    searchTerm = input("\nEnter a flower to search for: ")
    if searchTerm in flowerList:
        print(f"{searchTerm} was found in your list!")
    else:
        print(f"{searchTerm} was not found.")

    while True:
        try:
            choice = int(input("\nEnter a number to see the corresponding flower: "))
            # Adjust for list indexing
            print(f"You selected: {flowerList[choice - 1]}")
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError:
            print("Number out of range. Please try again.")
        except:  # Generic exception handling
            print("An unexpected error occurred.") 

if __name__ == "__main__":
    main()