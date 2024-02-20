class HeartRateTracker:
    def __init__(self):
        self.daily_heart_rates = {}
    def add_heart_rate(self, day, time_slot, heart_rate):
        if day in self.daily_heart_rates:
            if time_slot in self.daily_heart_rates[day]:
                self.daily_heart_rates[day][time_slot].append(heart_rate)
            else:
                self.daily_heart_rates[day][time_slot] = [heart_rate]
        else:
            self.daily_heart_rates[day] = {time_slot: [heart_rate]}
    def get_average_heart_rate(self, day, time_slot):
        if day in self.daily_heart_rates:
            if time_slot in self.daily_heart_rates[day]:
                heart_rates = self.daily_heart_rates[day][time_slot]
                return sum(heart_rates) / len(heart_rates)
            else:
                return None
        else:
            return None
def main():
    tracker = HeartRateTracker()
    while True:
        print("\n1. Add Heart Rate for a Time Slot\n2. View Average Heart Rate for a Time Slot\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            day = input("Enter the day: ")
            time_slot = input("Enter the time slot (morning, midday, afternoon, evening): ")
            heart_rate = int(input("Enter the heart rate: "))
            tracker.add_heart_rate(day, time_slot, heart_rate)
            print("Heart rate added successfully.")
        elif choice == "2":
            day = input("Enter the day: ")
            time_slot = input("Enter the time slot (morning, midday, afternoon, evening): ")
            average_heart_rate = tracker.get_average_heart_rate(day, time_slot)
            if average_heart_rate is not None:
                print(f"Average heart rate for {time_slot} on {day}: {average_heart_rate}")
            else:
                print(f"No data available for {time_slot} on {day}.")
        elif choice == "3":
            print("Exit.")
            break
        else:
            print("Wrong, enter a valid option.")
if __name__ == "__main__":
    main()
