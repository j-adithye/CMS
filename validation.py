import re
from datetime import datetime, date



def validate_role(role):
    if role in ['admin','receptionist','technician','pharmacist']:
        return True
    return False
def validate_username(user):
    if user in ['a','r','p','l']:
        return True
    if len(user)>5:
        return True
    return False

def validate_pwd(pwd):
    if pwd in ['a','r','p','l']:
        return True
    if len(pwd)>5:
        return True
    return False

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

def validate_date(date):
    pattern = r"\d{2}-\d{2}-\d{4}"
    if not re.fullmatch(pattern, date):
        return False
    else:
        try:
            date = datetime.strptime(date, "%d-%m-%Y").date()
        except ValueError:
            return False
        
        if date > datetime.today().date():
            return False

        return True

def validate_dob(dob):
    dob = datetime.strptime(dob, "%d-%m-%Y").date()
    today = date.today()

    age = today.year - dob.year

    # if birthday not yet this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return age >= 18