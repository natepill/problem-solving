
def reverse_string(string):
    ''' Non-cheeky way of reversing string'''
    output = ''

    for char in string:
        output = char + output

    return output


print(reverse_string('abc'))
