def reverse(x: int) -> int:
    # Will be returning an int

    string_int = str(x)

    result_string = ' '
    right = len(string_int)-1

    if string_int[0] == '-':
        result_string += string_int[0]

    while right != -1:

        if string_int[right] == '-':
            break

        result_string += string_int[right]
        right -= 1

    return int(result_string)


print(reverse(1534236469))
