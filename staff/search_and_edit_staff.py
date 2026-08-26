from data import staff_data as data
from validation import validate_name


def edit_staff(k,v):
    while True:
        print('''Which field do you want to edit?
            1. Address
            2. Name''')
        try:
            ch = input('Enter your choice: ').strip()
            if ch == '':
                raise ValueError('Choice cannot be empty')
            if not ch.isdigit():
                raise ValueError('Please enter a number')
            else:
                match int(ch):
                    case 1:
                        while True:
                            try:
                                address = input('Enter new address: ')
                                if address == '':
                                    raise ValueError('Address cannot be empty.')
                                else:
                                    v['address'] = address
                                    data[k] = v
                                    return
                            except ValueError as e:
                                print(e)
                    case 2:
                        while True:
                            try:
                                name = input('Enter new name: ')
                                if name == '':
                                    raise ValueError('Name cannot be empty.')
                                elif validate_name(name):
                                    v['name'] = name
                                    data[k] = v
                                    return
                                else:
                                    raise ValueError('Invalid Phone number.Try again...')
                            except ValueError as e:
                                print(e)
        except ValueError as e:
            print(e)

def disable_staff(k,v):
    while True:
        try:
            choice = input('Do you want to disable this patient(Y/n):').strip().lower()
            if choice == '':
                raise ValueError('Choice cannot be empty')
            if choice == 'y':
                v['is_active'] = False
                data[k] = v
                return
            elif choice == 'n':
                print('Patient not disabled. Returning to previous menu...')
                search_menu()
            else:
                print('Enter a valid choice. Try again...')
        except ValueError as e:
            print(e)

def view_search(k,v):
    print('\t\tCMS Patient View')
    print('\t   '+'='*25)
    print(f'Name: {v['name']}\t DOB: {v['dob']}\t Staff Registration Number: {k}')
    print(f'Phone: {v['phone']}\t\t Address: {v['address']}')
    print(f'Date of Joining: {v['doj']}\t Salary:{v['salary']}\t Is Active: {v['is_active']}')

    print('''\nHow would you like to proceed?
        1. Edit Staff
        2. Disable Staff
        3. Go Back''')
    try:
        ch = input('Enter your choice: ').strip()
        if ch == '':
            raise ValueError('Choice cannot be empty')
        if not ch.isdigit():
            raise ValueError('Please enter a number')
        else:
            match int(ch):
                case 1:
                    edit_staff(k,v)
                    return
                case 2:
                    disable_staff(k,v)
                    return
                case 3:
                    print('Returning to main menu....\n')
                    return
                case _:
                    print('Enter a valid number')
    except ValueError as e:
                print(e)


def search_reg():
    while True:
        try:
            reg_no = input('Enter Staff ID: ').strip()
            if reg_no == '':
                raise('Staff ID cannot be empty. Try again...')
            elif not reg_no.isdigit():
                raise ValueError('Staff ID should be a number')
            else:
                for k,v in data.items():
                    if k == int(reg_no):
                        view_search(k,v)
                        return
                print('Staff does not exist')
                return
        except ValueError as e:
            print(e)

def search_phone():
    while True:
        try:
            phone = input('Enter phone number: ').strip()
            if phone == '':
                raise('Phone number cannot be empty. Try again...')
            elif validate_phone(phone):
                for k,v in data.items():
                    if v['phone'] == phone:
                        view_search(k,v)
                        return
                print('Staff does not exist')
                return
            else:
                raise ValueError('Invalid phone number')
                
        except ValueError as e:
            print(e)


def search_menu():
    while True:
        print('''\n\nHow would you like to search for the staff?
            1. By Staff registration number
            2. By Phone number
            3. Go to Manage Patient Menu''')
        try:
            ch = input('Enter your choice: ').strip()
            if ch == '':
                 raise ValueError('Choice cannot be empty')
            if not ch.isdigit():
                raise ValueError('Please enter a number')
            else:
                match int(ch):
                    case 1:
                        search_reg()
                    case 2:
                        search_phone()
                    case 3:
                        print('Returning to main menu....\n')
                        return
                    case _:
                        print('Enter a valid number')
        except ValueError as e:
                    print(e)

