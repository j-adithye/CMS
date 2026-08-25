import re

def validate_username(user):
    return True

def validate_pwd(pwd):
    return True

def validate_name(name):
    pattern = r"^(?=(?:.*[A-Za-z]){3,}$)[A-Za-z]+(?: [A-Za-z]+)? [A-Za-z]+$"
    if re.match(pattern,name):
        return True
    return False

def validate_bloodgrp(bloodgrp):
    return True

def validate_phone(phone):
    return True

def validate_dob(dob):
    return True