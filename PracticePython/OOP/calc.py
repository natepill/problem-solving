

class Calculator(object):

    def __init__(self):
        pass

    def add(self, num1, num2):
        try:
            num1, num2 = float(num1), float(num2)

        except:
            return 'invalid input'


        try:
            return num1+num2
        except:
            return "Could not calcuate with given input"

    def subtract(self, num1, num2):
        try:
            num1, num2 = float(num1), float(num2)

        except:
            return 'invalid input'


        try:
            return num1-num2

        except:
            return "Could not calcuate with given input"


    def multiply(self, num1, num2):
        try:
            num1, num2 = float(num1), float(num2)

        except:
            return 'invalid input'

        try:
            return num1*num2

        except:
            return "Could not calcuate with given input"


    def divide(self, num1, num2):
        """ integer division """

        try:
            num1, num2 = float(num1), float(num2)

        except:
            return 'invalid input'

        try:
            return num1//num2

        except:
            return "Could not calcuate with given input"



if __name__ == "__main__":

    num1 = input("Enter num1: ")
    num2 = input("Enter num2: ")

    writing_input = True

    # create an array of operations from user input:
    # calculations = list()
    #
    # while writing_input:
    #
    #     input_val = input("enter value or operation: ")
    #     calculations.append(input_val)
        # writing_input

    calc = Calculator()

    print("ADD: ", calc.add(num1, num2))
    print("MUL: ", calc.multiply(num1, num2))
    print("SUB: ", calc.subtract(num1, num2))
    print("DIV: ", calc.divide(num1, num2))
