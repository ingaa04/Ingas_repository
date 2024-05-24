from Ueb5 import multiples

def test_1():
    assert multiples.multiples(10)!=0, "Number is not a multiple of 3!"
def test_2():
    assert multiples.multiples(15)==0, "Number is a multiple of 3!"
def test_3():
    assert multiples.multiples(30)==0, "Number is a multiple of 3!"
