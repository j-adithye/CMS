from data import medicine_data as data
from validation import validate_name


def edit_medicine(k,v):
    while True:
        print('''Which field do you want to edit?
            1. Quantity
            2. Price''')
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
                                qty = input('Enter Quantity in no of units: ').strip()
                                if qty == '':
                                    raise ValueError('Quantity cannot be empty. Try again...')
                                elif not qty.isdigit():
                                    raise ValueError('Enter number only...')
                                else:
                                    qty = int(qty)
                                    v['quantity'] = qty
                                    data[k] = v
                                    return
                            except ValueError as e:
                                print(e)
                    case 2:
                        while True:
                            try:
                                price = input('Enter Price in Rs: ').strip()
                                if price == '':
                                    raise ValueError('Price cannot be empty. Try again...')
                                elif not price.isdigit():
                                    raise ValueError('Enter number only...')
                                else:
                                    price = int(price)
                                    v['price'] = price
                                    data[k] = v
                                    return
                            except ValueError as e:
                                print(e)
        except ValueError as e:
            print(e)

def disable_medicine(k,v):
    while True:
        try:
            choice = input('Do you want to disable this Medicine(Y/n):').strip().lower()
            if choice == '':
                raise ValueError('Choice cannot be empty')
            if choice == 'y':
                v['is_active'] = False
                data[k] = v
                print('Medicine Disabled')
                return
            elif choice == 'n':
                print('Medicine not disabled. Returning to previous menu...')
                search_menu()
            else:
                print('Enter a valid choice. Try again...')
        except ValueError as e:
            print(e)

def view_search(k,v):
    print('\t\tCMS Medicine View')
    print('\t   '+'='*25)
    print(f'Medicine Name: {v['medicine name']}\t\t Medicine Registration Number: {k}')
    print(f'Company name: {v['company name']}\t\t Generic name: {v['generic name']}')
    print(f'Quantity: {v['quantity']}\t Price:{v['price']}\t Is Active: {v['is_active']}')

    print('''\nHow would you like to proceed?
        1. Edit Medicine
        2. Disable Medicine
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
                    edit_medicine(k,v)
                    return
                case 2:
                    disable_medicine(k,v)
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
            reg_no = input('Enter Medicine ID: ').strip()
            if reg_no == '':
                raise('Medicine ID cannot be empty. Try again...')
            elif not reg_no.isdigit():
                raise ValueError('Medicine ID should be a number')
            else:
                for k,v in data.items():
                    if k == int(reg_no):
                        view_search(k,v)
                        return
                print('Medicine does not exist')
                return
        except ValueError as e:
            print(e)

def search_name():
    while True:
        try:
            name = input('Enter medicine name: ').strip().capitalize()
            if name == '':
                raise ValueError('Medicine name cannot be empty. Try again...')
            else:
                break
        except ValueError as e:
            print(e)


def search_menu():
    while True:
        print('''\n\nHow would you like to search for the medicine?
            1. By Medicine ID
            2. By Medicine Name
            3. Go to Manage Medicine Menu''')
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
                        search_name()
                    case 3:
                        print('Returning to main menu....\n')
                        return
                    case _:
                        print('Enter a valid number')
        except ValueError as e:
                    print(e)

