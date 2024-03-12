import random

def main():
 
    secret_number = random.randint(1, 100)

   
    while True:
        try:
           
            guess = int(input("Guess a number between 1 and 100: "))

     
            if guess < 1 or guess > 100:
                raise ValueError("Guess must be between 1 and 100!")

     
            difference = abs(guess - secret_number)

         
            if difference <= 5:
                print("Very Hot!")
            elif difference <= 15:
                print("Hot!")
            elif difference <= 25:
                print("Cool!")
            else:
                print("Cold!")

            # Check if guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number: {secret_number}")
                break

        except ValueError as e:
            print("Invalid input:", e)

# Call the main function
if __name__ == "__main__":
    main()