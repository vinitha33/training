def is_Palindrome(str1):
    str2 = str1[::-1]
    if str1.lower() == str2.lower():
        return True
    else:
        return False

print(is_Palindrome(input("Enter the string:")))
