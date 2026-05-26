def test_validate1():
    x=40
    y=20
    assert (x>y)==True

def test_validate2():
    assert 20==20

def test_validate3():
    x=45
    assert x<=200

def test_validate4():
    s1="Programming"
    s2="Python Programming Language"
    assert s1 in s2

def test_validate5():
    s1="Programming"
    s2="Python Programming Language"
    assert s1 is s2 , "Match has not found"

def test_validate6():
    s1="Programming"
    s2="Programming"
    assert s1 in s2
