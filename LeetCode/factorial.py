

def factorial(number):
    """ Return factorial of number """

    if number == 1:
        return number

    return number * factorial(number-1)


def diff_factorial(number):
    print(number)
    for _ in range(0, number):
        print(number)
        number = number * number-1

    return number
    # for num in range(number, 0)





if __name__ == "__main__":

    number = 3
    print(diff_factorial(number))
