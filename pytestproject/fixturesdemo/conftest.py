
import pytest    

@pytest.fixture(scope = "function")
def setUp():
    print("Launch Browser and Navigate Application URL and Login into the Application")
    yield
    print("Logout from the Application and Close Browser")


@pytest.fixture(scope = "class")
def class_setup():
    print("Launch Browser and Navigate Application URL and Login into the Application: At Class Level")
    yield
    print("Logout from the Application and Close Browser : At Class Level")

@pytest.fixture(scope = "module")
def module_setup():
    print("Launch Browser and Navigate Application URL and Login into the Application: At Module Level")
    yield
    print("Logout from the Application and Close Browser : At Module Level")