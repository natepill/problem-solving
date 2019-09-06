
""" Not done """

def valid(parentheses):
    stack = []

    opening = {'(':')', '{':'}', '[':']'}

    for char in parentheses:
        # If current character is a closing parenthesis
        if stack[-1] == opening[char]:
            try:
                stack.pop()
            except:
                return False

        else:
            stack.append(char)

    return True


if __name__ == "__main__":
    valid_string = '{}()[]'
    invalid_string = "([)]"

    print(valid(valid_string))
    print(valid(invalid_string))
