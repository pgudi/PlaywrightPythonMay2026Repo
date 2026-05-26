import pytest

@pytest.mark.parametrize(
    "username, password",
    [("santosh","Welcome123"),("adams","Welcome123"),("jones","Welcome123"),("akshya","Welcome123")]
)

def test_login_params(username, password):
    print(username,"  -> ",password)