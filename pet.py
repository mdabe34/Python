class Pet:
    # Class variable
    vet_name = "Winding Creek Animal Hosptial"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self._owner_first_name = owner_first_name
        self._owner_last_name = owner_last_name
        self._pet_id = pet_id
        self._pet_name = pet_name
        self._pet_type = pet_type

    # Getter methods
    def get_owner_first_name(self):
        return self._owner_first_name

    def get_owner_last_name(self):
        return self._owner_last_name

    def get_pet_id(self):
        return self._pet_id

    def get_pet_name(self):
        return self._pet_name

    def get_pet_type(self):
        return self._pet_type

    # Setter methods
    def set_owner_first_name(self, first_name):
        self._owner_first_name = first_name

    def set_owner_last_name(self, last_name):
        self._owner_last_name = last_name

    def set_pet_id(self, pet_id):
        self._pet_id = pet_id

    def set_pet_name(self, pet_name):
        self._pet_name = pet_name

    def set_pet_type(self, pet_type):
        self._pet_type = pet_type

    # Method to display pet information
    def display_pet_info(self):
        print("Pet Information:")
        print("Owner:", self._owner_first_name, self._owner_last_name)
        print("Pet ID:", self._pet_id)
        print("Pet Name:", self._pet_name)
        print("Pet Type:", self._pet_type)
        print("Veterinary Office:", Pet.vet_name)
        print()

# Function to check property existence using hasattr()
def check_property(pet, property_name):
    if hasattr(pet, property_name):
        print(f"{property_name} exists for this pet.")
    else:
        print(f"{property_name} does not exist for this pet.")

# Pet class
pet1 = Pet("Dillon", "Putty", "4412", "Easton" , "Dog")
pet2 = Pet("Brayden", "Bakes", "2422", "Daisy", "Dog")
pet3 = Pet("Scott", "Maness", "2216", "Tyson" , "Dog")

# Displaying pet information
pet1.display_pet_info()
pet2.display_pet_info()
pet3.display_pet_info()

# Using setter method to update pet type for pet3
pet3.set_pet_type("Dog")

# Displaying updated information for pet3
print("After updating pet type for pet3:")
pet3.display_pet_info()

# Checking property existence using hasattr()
print("\nChecking property existence:")
check_property(pet1, "_pet_type")
check_property(pet2, "_pet_id")
check_property(pet3, "nonexistent_property")
