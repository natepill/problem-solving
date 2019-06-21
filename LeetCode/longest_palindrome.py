def find_longest_palindrome(string):
    ''' Return the longest palindrome in the given string'''

    longest_palindrome = None
    left = 0
    right = len(string)-1

    # increment the left bound up till the last index in the string
    while left != len(string)-1:

        # Start of potential palindrome
        if string[left] == string[right]:

            # Determine if the substring is a palindrome (Bool, String)
            result_palindrome = find_palindrome(string, left, right)

            # Substring was a palindrome
            if result_palindrome[0]:
                # Substring palindrome is longer than previously established longest_palindrome
                if len(result_palindrome[1]) > len(longest_palindrome):
                    longest_palindrome = result_palindrome[1]

            # Substring is not a palindrome
            else:
                left += 1
                right = len(string)-1

        # No potential palindrome match at current bounds
        else:
            right -= 1

    return longest_palindrome

def find_palindrome(string, left, right):
    ''' Is the given string a palindrome? Return: (Bool, String) '''

    substring_palindrome = ' '*(right-left)

    while left > right:
        # If characters match, then append and prepend both characters to the substring_palindrome
        if string[left] == string[right]:
            substring_palindrome[left] = string[left]
            substring_palindrome[right] = string[right]
        else:
            return (False, None)

        left += 1
        right -= 1

    return (True, substring_palindrome)


if __name__ == '__main__':

    string = "babad" # 'bab' or 'aba'

    print(find_longest_palindrome(string))
