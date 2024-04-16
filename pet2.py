class Pet:
    def __init__(self, kind, breed, name):
        self._kind = kind  
        self._breed = breed
        self._name = name

    def get_kind(self):
        return self._kind

    def set_kind(self, kind):
        self._kind = kind

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def print_details(self):
        print(f"Kind: {self._kind}")
        print(f"Breed: {self._breed}")
        print(f"Name: {self._name}")


# Instances
pet1 = Pet("dog", "Golden Retriever", "Bones")
pet2 = Pet("cat", "Persian", "Paul")
pet3 = Pet("bird", "Parakeet", "Beeky")

# Print out solutions
pet1.print_details()
print("---")
pet2.print_details()
print("---")
pet3.print_details()

# 3 special cases

# __name__
print(Pet.__name__)  
# getattr()
print(getattr(pet2, "_breed"))  
# isinstance()
print(isinstance(pet3, Pet)) 