import re
from datetime import datetime




def validate_username(user):
    return True

def validate_pwd(pwd):
    return True

def validate_name(name):
    pattern = r"^(?=(?:.*[A-Za-z]){3,}$)[A-Za-z]+(?: [A-Za-z]+)? [A-Za-z]+$"
    if re.fullmatch(pattern,name):
        return True
    return False

def validate_bloodgrp(bloodgrp):
    pattern = r"^(A|B|AB|O)[+-]$"
    if re.fullmatch(pattern,bloodgrp):
        return True
    return False

def validate_phone(phone):
    pattern = r"^[6-9]\d{9}$"
    if re.fullmatch(pattern,phone):
        return True
    return False

def validate_dob(dob):
    pattern = r"\d{2}-\d{2}-\d{4}"
    if not re.fullmatch(pattern, dob):
        return False
    else:
        try:
            date = datetime.strptime(dob, "%d-%m-%Y").date()
        except ValueError:
            return False
        
        if date > datetime.today().date():
            return False

        return True
