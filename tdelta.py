import datetime


def calculate_age(birth_date):
    

    today = datetime.date.today()
    age_in_days = (today - birth_date).days
    age_in_years = age_in_days // 365.25  


    days_remaining = age_in_days % 365.25     
    age_in_months = days_remaining // 30  
    days_remaining -= age_in_months * 30

    age_in_hours = days_remaining * 24
    age_in_minutes = age_in_hours * 60

    return age_in_years, age_in_months, int(days_remaining), int(age_in_hours), int(age_in_minutes)

def main():
    """Main function to get user input, calculate age, and display results."""

    while True:
        try:
            birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
            birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            break  
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    years, months, days, hours, minutes = calculate_age(birth_date)

    print(f"You are {years} years, {months} months, and {days} days old.")
    print(f"That's approximately {years * 365 + days} days, or {years * 365 * 24 + hours} hours, or {years * 365 * 24 * 60 + minutes} minutes!")


if __name__ == "__main__":
    main()