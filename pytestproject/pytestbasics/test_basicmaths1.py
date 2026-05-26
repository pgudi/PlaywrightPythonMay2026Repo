def multiplication(x,y):
    result=(x * y)
    return result


def test_mult1():
    assert multiplication(7,5)==35

def test_mult2():
    assert multiplication(-5, -10)==50

def test_mult3():
    assert multiplication(12,0)==0

def test_mult4():
    assert multiplication(-5, 9)==-45


