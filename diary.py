def main():

    date_time = input("Enter the current date and time (e.g., 2024-04-19 16:30): ")
    entry = input("Write your diary entry: ")

    with open("diary.txt", "a") as diary_file: #Open the dairy.txt file
        diary_file.write(date_time + "\n")
        diary_file.write(entry + "\n")
        diary_file.write("\n")  # Add an empty line to separate entries

    print("Diary entry saved!")

if __name__ == "__main__":
    main()