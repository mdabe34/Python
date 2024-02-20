def main():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    steps = [10000]

    # Prompt user to input steps walked for each day of the week
    for day in days_of_week:
        while True:
            try:
                steps_walked = int(input(f"Enter steps walked on {day}: "))
                if steps_walked < 0:
                    raise ValueError("Steps cannot be negative.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number of steps.")

        steps.append(steps_walked)

    # Calculate total steps walked
    total_steps = sum(steps)

    # Display total steps walked
    print("\nTotal steps walked during the week:")
    for day, steps_walked in zip(days_of_week, steps):
        print(f"{day}: {steps_walked} steps")
    print(f"Total: {total_steps} steps")

if __name__ == "__main__":
    main()