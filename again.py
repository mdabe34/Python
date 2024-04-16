class InvalidInputError(Exception):
    """Exception raised when the user provides invalid input."""
    pass

def main():
    while True:
        try:
            user_input = input("Enter a number: ")
            number = float(user_input)  

        except ValueError:  
            raise InvalidInputError("Invalid input. Please enter a number.")

        else: 
            print("You entered a valid number:", number)
            break  

        finally:
            print("End of input attempt.")

if __name__ == "__main__":
    main()