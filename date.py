import calendar
import datetime

def main():
    
    year = datetime.datetime.now().year  

    while True:
        try:
            birth_month = int(input("Enter your birth month (1-12): "))
            if 1 <= birth_month <= 12:
                break  
            else:
                print("Invalid month. Please enter a number between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a number.")

 
    my_calendar = calendar.month(year, birth_month)
    print(f"Calendar for Birth Month in {year}".center(20)) 
    print(my_calendar) 

if __name__ == "__main__":
    main()