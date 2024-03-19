def main():
    # Initialize an empty list to store book titles
    book_titles = []

    # Collect book titles using a while loop
    while len(book_titles) < 10:
        title = input("Enter a book title: ")
        book_titles.append(title)

    # Create a sorted list of book titles
    sorted_titles = sorted(book_titles)

    # Display the sorted book titles
    print("Sorted Book Titles:")
    for title in sorted_titles:
        print(title)

if __name__ == "__main__":
    main()