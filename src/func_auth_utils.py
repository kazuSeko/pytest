def is_strong_password(password):
    """
     The length of password should be at least 8 charactors.
    """

    if not isinstance(password, str):
        return False

    if len(password) < 8:
        return False
    else:
        return True