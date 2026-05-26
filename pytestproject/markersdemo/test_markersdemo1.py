import pytest

@pytest.mark.sanity
def test_testcase1():
    print("It is a First Pytest Testcase")

@pytest.mark.sanity
def test_testcase2():
    print("It is a Second Pytest Testcase")

@pytest.mark.api
def test_testcase3():
    print("It is a Third Pytest Testcase")

@pytest.mark.api
def test_testcase4():
    print("It is a Fourth Pytest Testcase")

@pytest.mark.regression
def test_testcase5():
    print("It is a Fifth Pytest Testcase")

@pytest.mark.regression
def test_testcase6():
    print("It is a Sixth Pytest Testcase")

@pytest.mark.database
def test_testcase7():
    print("It is a Seventh Pytest Testcase")

@pytest.mark.database
def test_testcase8():
    print("It is a Eighth Pytest Testcase")