import Calculator

def test_add():
    x = 10
    y = 25
    result = Calculator.add(x, y)
    assert x+y == result

def test_sub():
    x = 20
    y = 10
    result = Calculator.sub(x, y)
    assert x-y == result

def test_multi():
    x = 20
    y = 10
    result = Calculator.multi(x, y)
    assert x*y == result

def test_div():
    x = 20
    y = 10
    result = Calculator.div(x, y)
    assert x/y == result