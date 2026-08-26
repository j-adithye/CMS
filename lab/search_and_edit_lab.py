from data import test_data as data
from validation import validate_name


def edit_test(k,v):
    while True:
        print('''Which field do you want to edit the Price''')
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

def disable_test(k,v):
    while True:
        try:
            choice = input('Do you want to disable this test(Y/n):').strip().lower()
            if choice == '':
                raise ValueError('Choice cannot be empty')
            if choice == 'y':
                v['is_active'] = False
                data[k] = v
                return
            elif choice == 'n':
                print('test not disabled. Returning to previous menu...')
                search_menu()
            else:
                print('Enter a valid choice. Try again...')
        except ValueError as e:
            print(e)

def view_search(k,v):
    print('\t\tCMS test View')
    print('\t   '+'='*25)
    print(f'test Name: {v['name']}\t\t test Registration Number: {k}')
    print(f'Low Range: {v['low range']}\t\t High Range: {v['high range']}\t Unit: {v['unit']}')
    print(f' Price:{v['price']}\t Is Active: {v['is_active']}')

    print('''\nHow would you like to proceed?
        1. Edit test
        2. Disable test
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
                    edit_test(k,v)
                    return
                case 2:
                    disable_test(k,v)
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
            reg_no = input('Enter test ID: ').strip()
            if reg_no == '':
                raise('Test ID cannot be empty. Try again...')
            elif not reg_no.isdigit():
                raise ValueError('Test ID should be a number')
            else:
                for k,v in data.items():
                    if k == int(reg_no):
                        view_search(k,v)
                        return
                print('Test does not exist')
                return
        except ValueError as e:
            print(e)


def search_menu():
    while True:
        print('''\n\nHow would you like to search for the test?
            1. By test ID
            2. Go to Manage test Menu''')
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
                    case 3:
                        print('Returning to main menu....\n')
                        return
                    case _:
                        print('Enter a valid number')
        except ValueError as e:
                    print(e)

