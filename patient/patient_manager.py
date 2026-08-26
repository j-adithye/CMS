from validation import validate_name,validate_bloodgrp,validate_phone,validate_date
from patient.search_and_edit_patient import search_menu
from datetime import datetime
from data import patients_data
from logs.log_manager import add_logs



def add_patient(user):
    print('Adding New Patient')
    while True:
        try:
            name = input('Enter Full name: ').strip().capitalize()
            if name == '':
                raise ValueError('Full name cannot be empty. Try again...')
            else:
                if validate_name(name):
                    break
                else:
                    raise ValueError('Invalid name. Try again...')
        except ValueError as e:
            print(e)

    while True:
        try:
            phone = input('Enter phone number: ').strip()
            if phone == '':
                raise('Phone number cannot be empty. Try again...')
            elif validate_phone(phone):
                break
            else:
                raise ValueError('Invalid phone number')
        except ValueError as e:
            print(e)

    for k,v in patients_data.items():
        if v['phone'] == phone and v['name'] == name:
            print('Patient alredy exists with Registration number:',k)
            return

    while True:
        try:
            dob = input('Enter Date of Birth: ').strip()
            if dob == '':
                raise ValueError('DOB cannot be empty. Try again...')
            elif validate_date(dob):
                break
            else:
                raise ValueError('Date of Birth should in format DD-MM-YYYY. Try again...')
        except ValueError as e:
            print(e)

    while True:
        try:
            bloodgrp = input('Enter Blood Group(eg: A+, B-, etc...): ').strip().upper()
            if bloodgrp == '':
                raise ValueError('Blood Group cannot be empty. Try again...')
            else:
                if validate_bloodgrp(bloodgrp):
                    break
                else:
                    raise ValueError('Invalid blood group. Try again...')
        except ValueError as e:
            print(e)

    while True:
        try:
            address = input('Enter Address: ').strip()
            if address == '':
                raise ValueError('Address cannot be empty.Try again...')
            else:
                break
        except ValueError as e:
            print(e)

    while True:
        try:
            gender = input('Enter Gender(M/F/O): ').strip().upper()
            if gender == ''or gender not in ['F','M','O']:
                raise ValueError('Invalid gender. Try again...')
            else:
                break
        except ValueError as e:
            print(e)


    if not patients_data:
        new_id = 100001
    else:
        new_id = next(reversed(patients_data)) + 1
    patients_data[new_id] = {'name':name, 'dob': dob, 'blood group': bloodgrp, 'gender':gender, 'phone': phone, 'address': address, 'created on': datetime.today().date().strftime("%d-%m-%Y"), 'is_active': True}

    print('Successfully Added with Registration ID: ',new_id)

    message = f"New Patient with ID-{new_id} was added by Receptionist-{user}"
    add_logs(message)




def list_patients():
    print('Patient ID\t Name\t\t DOB\t Blood Group\t Gender\t Phone Num\t Address\t Created On\t Is Active')
    for k,v in patients_data.items():
        print(f'{k}\t\t{v['name']}\t {v['dob']}\t {v['blood group']}\t {v['gender']}\t {v['phone']}\t {v['address']}\t {v['created on']}\t {v['is_active']}')

    print('END OF LIST...')
    return
    

def manage_patients_menu(user):
    while True:
        print('\n\t\t CMS Manage Patient Menu')
        print('\t\t************************')
        print('\t\tWelcome ',user)
        print('''What would you like to do?
                1. Add Patients
                2. View list of Patients
                3. Search and View Patient
                4. Main Menu''')
        try:
            ch = input('Enter your choice: ').strip()
            if not ch.isdigit():
                raise ValueError('Please enter a number')
            else:
                match int(ch):
                    case 1:
                        add_patient(user)
                    case 2:
                        list_patients()
                    case 3:
                        search_menu()    
                    case 4:
                        print('Returning to main menu....\n')
                        return
                    case _:
                        print('Enter a valid number')
        except ValueError as e:
            print(e)