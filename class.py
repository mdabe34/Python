class Person:
    def __init__(self, name, address, age, phone_number):
        self._name = name
        self._address = address
        self._age = age
        self._phone_number = phone_number

    
    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_age(self):
        return self._age

    def get_phone_number(self):
        return self._phone_number

    # Mutator methods (setters)
    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_age(self, age):
        self._age = age

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

# Person class
person1 = Person("Ferris Bueller", "370 Beech Street, Highland Park, IL", 18, "312-499-8795")
person2 = Person("Elwood Blues", "1060 W Addison Street, Chicago, IL", 34, "773-202-5678")
person3 = Person("Andy Dusfrene", "100 Reformatory Road, Portland, ME", 42, "911")


print("Name:", person1.get_name())
print("Address:", person1.get_address())
print("Age:", person1.get_age())
print("Phone Number:", person1.get_phone_number())
print()


print("Name:", person2.get_name())
print("Address:", person2.get_address())
print("Age:", person2.get_age())
print("Phone Number:", person2.get_phone_number())
print()


print("Name:", person3.get_name())
print("Address:", person3.get_address())
print("Age:", person3.get_age())
print("Phone Number:", person3.get_phone_number())
