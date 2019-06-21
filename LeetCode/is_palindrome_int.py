def isPalindrome(x: int) -> bool:

    string_int = str(x)
    left = 0
    right = len(string_int)-1

    while left < right:

        if string_int[left] != string_int[right]:
            return False

        left += 1
        right -= 1

    return True


print(isPalindrome(212))
