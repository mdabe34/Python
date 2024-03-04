def calculate_bmi(weight_pounds, height_inches):
 

 # Check for valid inputs from the user
 if not isinstance(weight_pounds, (int, float)) or weight_pounds <= 0:
   raise ValueError("Weight must be a positive number.")
 if not isinstance(height_inches, (int, float)) or height_inches <= 0:
   raise ValueError("Height must be a positive number.")

 # Convert weight in pounds to kilograms
 weight_kg = weight_pounds * 0.453592

 # Convert height in inches to meters
 height_m = height_inches * 0.0254

 # Calculate BMI
 bmi = weight_kg / (height_m * height_m)

 # To Find which category their bmi falls under
 if bmi < 18.5:
   category = "Underweight"
 elif bmi < 25:
   category = "Normal weight"
 elif bmi < 30:
   category = "Overweight"
 else:
   category = "Obese"

 return bmi, category

# Get user input for their height and weight
try:
 weight_pounds = float(input("Enter your weight in pounds: "))
 height_inches = float(input("Enter your height in inches: "))

 # Calculate and interpret BMI
 bmi, category = calculate_bmi(weight_pounds, height_inches)

 print(f"Your BMI is: {bmi:.2f}")
 print(f"BMI category: {category}")

except ValueError as e:
 print("Error:", e)