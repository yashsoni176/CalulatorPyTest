import Calculator
import pytest

@pytest.mark.xfail
@pytest.mark.parametrize("a,b,c",[(3,2,5),(4,6,11),(7,8,16),(10,12,22)])
def test_add(a,b,c):
    result = Calculator.add(a,b)
    assert c == result

@pytest.mark.parametrize("a,b,c",[(3,2,1),(4,6,-2),(7,8,-1),(10,12,-2)])
def test_sub(a,b,c):
    result = Calculator.sub(a,b)
    assert c == result

@pytest.mark.parametrize("a,b,c",[(3,2,6),(4,6,24),(7,8,56),(10,12,120)])
def test_multi(a,b,c):
    result = Calculator.multi(a,b)
    assert c == result

@pytest.mark.parametrize("a,b,c",[(4,2,2),(10,5,2),(7,7,1),(10,1,10)])
def test_div(a,b,c):
    result = Calculator.div(a,b)
    assert c == result