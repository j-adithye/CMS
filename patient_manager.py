from menu import menu
from validation import validate_name,validate_bloodgrp,validate_phone

patients_data = {}


def add_patient():
    print('Add New Patient')
    while True:
        try:
            name = input('Enter Full name: ').strip()
            if name == '':
                raise ValueError('Full name cannot be empty. Try again...')
            else:
                if validate_name():
                    break
                else:
                    raise ValueError('Invalid name. Try again...')
        except ValueError as e:
            print(e)


    while True:
        try:
            age = input('Enter Age: ').strip()
            if name == '':
                raise ValueError('Age cannot be empty. Try again...')
            elif age.isdigit():
                age = int(age)
                if age < 0 or age > 120:
                    raise ValueError('Age should be between 0 and 120')
                else:
                    break
            else:
                raise ValueError('Age should be a number. Try again...')
        except ValueError as e:
            print(e)

    while True:
        try:
            bloodgrp = input('Enter Blood Group(eg: A+, B-, etc...): ').strip().upper()
            if name == '':
                raise ValueError('Blood Group cannot be empty. Try again...')
            else:
                if validate_bloodgrp():
                    break
                else:
                    raise ValueError('Invalid blood group. Try again...')
        except ValueError as e:
            print(e)

    while True:
        try:
            phone = input('Enter phone number: ').strip()
            if validate_phone(phone):
                break
            else:
                raise ValueError('Invalid phone number')
        except ValueError as e:
            print(e)

    while True:
        try:
            address = input('Enter Address: ').strip()
            if address == '':
                raise ValueError('Address cannot be empty')
            else:
                break
        except ValueError as e:
            print(e)

    
def list_patients():
    pass

def search_patient():
    pass




def manage_patients_menu():
    print('\n\t\t CMS Manage Patient Menu')
    print('\t\t************************')
    print('''What would you like to do?
            1. Add Patients
            2. View list of Patients
            3. Search and View Patient
            4. Main Menu''')
    while True:
        try:
            ch = input('Enter your choice: ').strip()
            if not ch.isdigit():
                raise ValueError('Please enter a number')
            else:
                match int(ch):
                    case 1:
                        add_patient()
                    case 2:
                        list_patients()
                    case 3:
                        search_patient()    
                    case 4:
                        print('Returning to main menu....\n')
                        menu()
                    case _:
                        print('Enter a valid number')
        except ValueError as e:
            print(e)