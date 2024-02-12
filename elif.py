# Define a function to calulate a letter grade based on Percentage 
# Get the precentage correct of the assignment
percentage = int(input("What is the Percentage of the assignment?"))
# Check the percentage of answers correct
if percentage > 100:
    print("You have an A.") # Student scored an A on the assignment.
elif percentage > 90:
    print("You have a A.") # Student scored a B on the assignment.
elif percentage > 80:
    print("You have a B.") # Student scored a C on the assignment.
elif percentage > 70:
    print("You have a C.") # Student scored a D on the assignment.
elif percentage > 60:
    print("You have an D.") # Student scored an F on the assignment.
elif percentage > 0:
    print("You have an F.")
