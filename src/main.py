from func_add import add
from func_auth_utils import is_strong_password


if __name__ == "__main__":
    result = add(2,4)
    print("result:",result)

    pw = "pystar123"
    if is_strong_password(pw):
        print("password is ok.")
    else:
        print("password is too weak. Password should be at least 8 charactors.")
