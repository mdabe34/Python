# Define variables for Pound values
kg_value_1 = 25.4
kg_value_2 = 50.8
kg_value_3 = 76.2
kg_value_4 = 101.6

# Conversion factor: 2.20462 Pound = 1 Kilograms
conversion_factor = 2.20462

# Calculate inches for each centimeter value
pound_1 = kg_value_1 / conversion_factor
pound_2 = kg_value_2 / conversion_factor
pound_3 = kg_value_3 / conversion_factor
pound_4 = kg_value_4 / conversion_factor

# Output the results
print(f"{kg_value_1} pounds is equal to {pound_1:.2f} kilograms.")
print(f"{kg_value_2} pounds is equal to {pound_2:.2f} kilograms.")
print(f"{kg_value_3} pounds is equal to {pound_3:.2f} kilograms.")
print(f"{kg_value_4} pounds is equal to {pound_4:.2f} kilograms.")
