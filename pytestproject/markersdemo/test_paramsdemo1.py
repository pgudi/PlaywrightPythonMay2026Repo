import pytest

@pytest.mark.parametrize(
    "x, y, result",
    [(10,20,30),(5,10,15),(100,50,150)]
)

def test_add_validation(x,y,result):
    assert (x + y) == result




