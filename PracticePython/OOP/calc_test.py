"""
Notes:

    Fixtures:
    are functions that run before each test function
    Can act as a baseline for running test to make sure the enviorement is fixed
    @pytest.fixture

    Testing external functions:





"""


from calc import Calculator

def test_add():
    calc = Calculator()

    assert calc.add(5, 5) == 10
    assert calc.add(5, -5) == 0
    assert calc.add(5, '$') == 'invalid input'


def test_sub():
    calc = Calculator()

    assert calc.subtract(5, 5) == 0
    assert calc.subtract(5, -5) == 10
    assert calc.subtract(5,'$') == 'invalid input'

def test_mul():
    calc = Calculator()

    assert calc.multiply(5, 5) == 25
    assert calc.multiply(5, -5) == -25
    assert calc.multiply(5,'$') == 'invalid input'

def test_div():

    calc = Calculator()

    assert calc.divide(5, 5) == 1
    assert calc.divide(5, -5) == -1
    assert calc.divide(5, 3) == 1
    assert calc.divide(5, -3) == -2
    assert calc.divide(5, '$') == 'invalid input'
    assert calc.divide(5, 0) == "Could not calcuate with given input"
