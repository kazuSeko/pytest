from src.func_auth_utils import is_strong_password

def test_password_lengh_ok():
    assert is_strong_password("12345678") == True

def test_password_lengh_long_string():
    assert is_strong_password("12345678910111213") == True

def test_password_lengh_long_int():
    assert is_strong_password(12345678910111213) == False

def test_password_lengh_ng():
    assert is_strong_password("1234567") == False

def test_password_lengh_short():
    assert is_strong_password("1234") == False

def test_password_empty():
    assert is_strong_password("") == False
