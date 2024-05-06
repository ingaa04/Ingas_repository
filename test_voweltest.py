
from Ueb5 import voweltest
def test_1():
    assert voweltest.vowels('Hallo'), "Es gibt 2 Vokale!"

def test_2():
    assert voweltest.vowels('hkslwp')== 0, "Es gibt 0 Vokale!"

def test_3():
    assert voweltest.vowels('einen wunderschoenen guten morgen'), "Es gibt 12 Vokale!"