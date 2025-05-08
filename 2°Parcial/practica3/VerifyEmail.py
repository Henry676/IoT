import re

def validateEmail(email):
    """
    Metodo para validacion de un correo electronico mediante REGEX

    """
    #regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    regex = r"^(?!.*\.\.)([a-zA-Z0-9]+[a-zA-Z0-9._+-]*[a-zA-Z0-9]+)@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"

    if not email:
        return False

    if not re.match(regex, email):
        return False

    return True
