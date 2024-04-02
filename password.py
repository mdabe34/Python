def main():
        valid = False 
        while not valid:
            valid = True 
            print("""Password Requirements:\n
                  Between 8 to 20 characters long.\n
                  Contains at least one uppercase letter.\n
                  Contains at least one lowercase letter.\n
                  Includes at least one number.\n
                  Includes at least one symbol from the set: !@#$%&*\n""")

            password = input("Please enter a password that meets the criteria: ")
            length = len (password)
            if 7 < length < 21:
                continue
            else:
                valid = False
                print("That password is not the right length")

            is_upper = False 

            has_symbol = False
            symbol = ['!', '@', '#']
            for s in symbol:
                for c in password:
                    if s == c:
                        has_symbol == True
            if has_symbol == False:
                print("you need to include a symbol")
                valid = False
                continue

def get_valid_password():
    """Prompts user for password and checks it against criteria"""
    while True:
        password = input("Enter a password (8-20 characters, uppercase, lowercase, number, symbol): ")
        
        has_length = 8 <= len(password) <= 20
        has_upper = False
        has_lower = False
        has_number = False
        has_symbol = False

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_number = True
            elif char in "!@#$%&*":
                has_symbol = True

        if has_length and has_upper and has_lower and has_number and has_symbol:
            return password
        else:
            print("Invalid password. Please ensure it meets all criteria.")

if __name__ == "__main__":
    main()