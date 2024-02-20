def initialize_seats():
    return [0] * 20  # Show all seats as available (0 represents available)

def buy_ticket(seats):
    available_seats = [i + 1 for i, seat in enumerate(seats) if seat == 0]
    if available_seats:
        print("Available seats:", available_seats)
        seat_number = int(input("Enter the seat number you want to purchase (1-20): "))
        if seat_number in available_seats:
            seats[seat_number - 1] = 1  # Mark seat as sold (1 represents sold)
            print(f"Ticket for seat {seat_number} purchased successfully.")
        else:
            print("Seat not available.")
    else:
        print("All seats are sold out.")

def view_available_seats(seats):
    available_seats = [i + 1 for i, seat in enumerate(seats) if seat == 0]
    print("Available seats:", available_seats)

def view_sales_report(seats):
    sold_seats = [i + 1 for i, seat in enumerate(seats) if seat == 1]
    print("Seats sold:", sold_seats)
    print(f"Total tickets sold: {len(sold_seats)}")
    print(f"Total revenue: ${len(sold_seats) * 20}")

def main():
    seats = initialize_seats()
    while True:
        print("\n1. Buy Ticket\n2. View Available Seats\n3. View Sales Report\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            buy_ticket(seats)
        elif choice == "2":
            view_available_seats(seats)
        elif choice == "3":
            view_sales_report(seats)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("This option isn't available.")

if __name__ == "__main__":
    main()
