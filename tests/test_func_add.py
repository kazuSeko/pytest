from src.func_add import add

def test_add_success():
    assert add(2,4) == 6

def test_add_negative():
    assert add(-2,-4) == 0

def test_add_zero():
    assert add(0,0) == 0