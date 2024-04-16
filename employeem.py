#Employee Main
def main():
    print("Enter the following details of the Employee")
    print("--------------------------------------------")
    name = input("Enter Employee Name: ")
    number = input("Enter Employee Number: ")
    shift_number = int(input("Enter Shift Number (1 for day, 2 for night): "))
    pay_rate = float(input("Enter Pay Rate: "))

    worker = ProductionWorker(name, number, shift_number, pay_rate)

    print("\n-------------------------------------------------------")
    print("Details of Employee:")
    print("-------------------------------------------------------")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_number())
    print("Shift:", "Day" if worker.get_shift_number() == 1 else "Night") 
    print("Pay Rate:", worker.get_pay_rate())

if __name__ == "__main__":
    main()

#Employee Classes
class Employee:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, pay_rate):
        super().__init__(name, number)
        self._shift_number = shift_number
        self._pay_rate = pay_rate

    def get_shift_number(self):
        return self._shift_number

    def set_shift_number(self, shift_number):
        self._shift_number = shift_number

    def get_pay_rate(self):
        return self._pay_rate

    def set_pay_rate(self, pay_rate):
        self._pay_rate = pay_rate
