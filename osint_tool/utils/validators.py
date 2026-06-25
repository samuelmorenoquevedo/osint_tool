import phonenumbers
from email_validator import validate_email, EmailNotValidError

def validar_telefono(numero):
    try:
        parsed = phonenumbers.parse(numero, None)
        return phonenumbers.is_valid_number(parsed)
    except:
        return False

def validar_email(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False
