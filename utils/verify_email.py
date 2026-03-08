import re
def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao, email) is not None

def verify_in_json(email, usuarios):
    return any(u["email"] == email for u in usuarios)
     