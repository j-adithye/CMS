from validation import validate_name,validate_bloodgrp,validate_phone,validate_dob

patients_data = {1001:{'name':'Sumesh Kumar', 'age': 25, 'blood group': 'O+', 'phone': 9656244560, 'address': 'Trivandrum'}}


def add_patient():
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
            dob = input('Enter Age: ').strip()
            if dob == '':
                raise ValueError('Age cannot be empty. Try again...')
            elif validate_dob(dob):
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
            phone = input('Enter phone number: ').strip()
            if phone == '':
                raise('Phone number cannot be empty. Try again...')
            elif validate_phone(phone):
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

    if not patients_data:
        new_id = 1001
    else:
        new_id = next(reversed(patients_data)) + 1
    patients_data[new_id] = {'name':name, 'dob': dob, 'blood group': bloodgrp, 'phone': phone, 'address': address}

    print('Successfully Added with Registration ID: ',new_id)
    
def list_patients():
    print('Patient ID\t Name\t\t DOB\t Blood Group\t Phone Num\t Address')
    for k,v in patients_data.items():
        print(f'{k}\t\t{v['name']}\t {v['dob']}\t {v['blood group']}\t\t {v['phone']}\t {v['address']}')

    print('END OF LIST...')
    return
    



def search_patient():
    pass




def manage_patients_menu():
    while True:
        # print("\033[H\033[J", end="")
        print('\n\t\t CMS Manage Patient Menu')
        print('\t\t************************')
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
                        add_patient()
                    case 2:
                        list_patients()
                    case 3:
                        search_patient()    
                    case 4:
                        print('Returning to main menu....\n')
                        return
                    case _:
                        print('Enter a valid number')
        except ValueError as e:
            print(e)