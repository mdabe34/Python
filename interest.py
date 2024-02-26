def calculate_interest(principal, rate, time):
    simpleInterest = (principal*rate*time)/100
    print(f"The simple interest for a principal amount of {principal} \
          at an interest rate of {rate}% over a period of {time} years is : {simpleInterest}")
input_principal = int(input("Enter the principal amount: "))
input_rate = float(input("Enter the rate of interest as a %: "))
input_time = int(input("Enter the time amount in whole years: "))
calculate_interest(principal=input_principal, rate=input_rate, time=input_time)