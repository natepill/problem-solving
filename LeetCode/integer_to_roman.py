def intToRoman(num) -> str:
    ''' Covert integer to roman numeral '''

    roman_dict = {
    'M':1000,
    'D':500,
    'C':100,
    'L':50,
    'X':10,
    'V':5,
    'I':1
    }

    numeral_dict = {
    1000:'M',
    500:'D',
    100:'C',
    50:'L',
    10:'X',
    5:'V',
    1:'I'
    }

    # Roman numeral representation of number
    result = ''


    for value in numeral_dict.keys():

        if num == 0:
            break
        # num < value
        if num%value != num:
            result += numeral_dict[value]
            num = num%value

    return result

if __name__ == "__main__":

    number = 198
    print(intToRoman(number))
