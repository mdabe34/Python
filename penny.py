def isPalindrome(string):
    if (string == string[::-1]):
        return f"{string} is a palindrome."
    else:
        return f"{string} is not a palindrome."
   
string = input("Enter string: ")
print(isPalindrome(string))