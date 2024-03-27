# Python String Methods Practice

# TODO: Use the capitalize() method to capitalize the first letter of the string
# Example: "python" -> "Python"
string1 = "python"
string1 = string1.capitalize()


# TODO: Use the center() method to center the string in a string of specified width
# Example: "python" -> "  python  "
string2 = "python"
string2 = string2.center(10)

# TODO: Use the endswith() method to check if the string ends with a specified substring
# Example: Check if "python" ends with "on"
string3 = "python"
ends_with_on = string3.endswith("on")

# TODO: Use the find() method to find the first occurrence of a substring in the string
# Example: Find the position of "th" in "python"
string4 = "python"
pos_of_th = string4.find("th")

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
# Example: Check if "python3" is alphanumeric
string5 = "python3"
is_alphanumeric = string5.isalnum()

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
# Example: Check if "python" is alphabetic
string6 = "python"
is_alphabetic = string6.isalpha()

# TODO: Use the islower() method to check if all characters in the string are lowercase
# Example: Check if "python" is in lowercase
string7 = "python"
is_lowercase = string7.islower()

# TODO: Use the isspace() method to check if all characters in the string are whitespaces
# Example: Check if "  " is all whitespace
string8 = "  "
is_all_whitespace = string8.isspace()  # Output: True

# TODO: Use the isupper() method to check if all characters in the string are uppercase
# Example: Check if "PYTHON" is in uppercase
string9 = "PYTHON"
is_uppercase = string9.isupper()  # Output: True

# TODO: Use the join() method to join elements of an iterable with the string as the separator
# Example: Join ["Python", "is", "fun"] with "-" as separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
joined_string = separator.join(iterable1)  # Output: "Python-is-fun"

# TODO: Use the lower() method to convert all characters in the string to lowercase
# Example: Convert "PYTHON" to lowercase
string10 = "PYTHON"
string10 = string10.lower()  # Output: "python"

# TODO: Use the lstrip() method to remove leading characters (spaces by default)
# Example: Remove leading spaces from " python"
string11 = "  python"
string11 = string11.lstrip()  # Output: "python"

# TODO: Use the rstrip() method to remove trailing characters (spaces by default)
# Example: Remove trailing spaces from "python "
string12 = "python  "
string12 = string12.rstrip()  # Output: "python"

# TODO: Use the replace() method to replace all occurrences of a substring with another substring
# Example: Replace "python" with "snake" in "I love python"
string13 = "I love python"
string13 = string13.replace("python", "snake")  # Output: "I love snake"

# TODO: Use the rfind() method to find the highest index of a substring
# Example: Find the highest index of "n" in "python"
string14 = "python"
highest_index_of_n = string14.rfind("n")  # Output: 5

# TODO: Use the split() method to split the string at a specified separator
# Example: Split "python-is-fun" at "-"
string15 = "python-is-fun"
split_list = string15.split("-")  # Output: ["python", "is", "fun"]

# TODO: Use the startswith() method to check if the string starts with a specified substring
# Example: Check if "python" starts with "py"
string16 = "python"
starts_with_py = string16.startswith("py")  # Output: True

# TODO: Use the strip() method to remove both leading and trailing characters (spaces by default)
# Example: Remove spaces from " python "
string17 = "  python  "
string17 = string17.strip()  # Output: "python"

# TODO: Use the swapcase() method to swap the case of all characters in the string
# Example: Swap case of "Python"
string18 = "Python"
string18 = string18.swapcase()  # Output: "pYTHON"

# TODO: Use the title() method to convert the first character of each word to uppercase
# Example: Convert "python is fun" to title case
string19 = "python is fun"
string19 = string19.title()  # Output: "Python Is Fun"

# TODO: Use the upper() method to convert all characters in the string to uppercase
# Example: Convert "python" to uppercase
string20 = "python"
string20 = string20.upper()  # Output: "PYTHON"