from validation import validate_name,validate_phone,validate_date
from data import staff_data
from staff.search_and_edit_staff import search_menu
from logs.log_manager import add_logs


def add_staff(user):
    print('Adding New Staff')
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

    for k,v in staff_data.items():
        if v['phone'] == phone and v['name'] == name:
            print('Staff alredy exists with Staff ID:',k)
            return

    while True:
        try:
            dob = input('Enter Age: ').strip()
            if dob == '':
                raise ValueError('Age cannot be empty. Try again...')
            elif validate_date(dob):
                break
            else:
                raise ValueError('Date of Birth should in format DD-MM-YYYY. Try again...')
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
            doj = input('Enter Date of Joining: ').strip()
            if doj == '':
                raise ValueError('DOJ cannot be empty. Try again...')
            elif validate_date(doj):
                break
            else:
                raise ValueError('Date of Joining should in format DD-MM-YYYY. Try again...')
        except ValueError as e:
            print(e)

    while True:
        try:
            salary = input('Enter salary in Rs: ').strip()
            if salary == '':
                raise ValueError('Salary cannot be empty. Try again...')
            elif not salary.isdigit():
                raise ValueError('Enter number only...')
            else:
                salary = int(salary)
                break
        except ValueError as e:
            print(e)


    if not staff_data:
        new_id = 1001
    else:
        new_id = next(reversed(staff_data)) + 1
    staff_data[new_id] = {'name':name, 'dob': dob, 'phone': phone, 'address': address,'doj': doj,'salary': salary, 'is_active': True}

    print('Successfully Added with Staff ID: ',new_id)
    message = f"New Staff with ID-{new_id} was added by Admin-{user}"
    add_logs(message)


def list_staff():
    print('Staff ID\t Name\t\t DOB\t Phone Num\t Address\t DOJ\t Salary\t Is Active')
    for k,v in staff_data.items():
        print(f'{k}\t\t{v['name']}\t {v['dob']}\t\t {v['phone']}\t {v['address']}\t {v['doj']}\t {v['salary']}\t {v['is_active']}')

    print('END OF LIST...')
    return


def manage_staff_menu(user):
    
    while True:
        # print("\033[H\033[J", end="")
        print('\n\t\t CMS Manage Patient Menu')
        print('\t\t************************')
        print('\t\tWelcome ',user)
        print('''What would you like to do?
                1. Add Staff
                2. View list of Staff
                3. Search and View Staff
                4. Main Menu''')
        try:
            ch = input('Enter your choice: ').strip()
            if not ch.isdigit():
                raise ValueError('Please enter a number')
            else:
                match int(ch):
                    case 1:
                        add_staff(user)
                    case 2:
                        list_staff()
                    case 3:
                        search_menu()    
                    case 4:
                        print('Returning to main menu....\n')
                        return
                    case _:
                        print('Enter a valid number')
        except ValueError as e:
            print(e)
