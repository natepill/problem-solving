def palindrome(name):
    
    palindrome = name[::-1]
    if palindrome == name:
        print("True")
        return True
    else:
        print("False")
        return False


palindrome("hannah")
