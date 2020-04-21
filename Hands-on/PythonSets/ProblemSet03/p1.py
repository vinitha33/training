def is_palindrome(string):
    cp_string=string[::-1]
    if cp_string==string:
        return True
    else:
        return False
print(is_palindrome(str(input())))