from data import test_data as data
from lab.search_and_edit_lab import search_menu
from logs.log_manager import add_logs


def list_test():
    print('test ID\t test name\t Low Range\t High Range\t UNit\t Price\t Is Active')
    for k,v in data.items():
        print(f'{k}\t  {v['test name']}\t\t {v['low range']}\t\t {v['high range']}\t\t {v['unit']}\t {v['price']}\t {v['is_active']}')

    print('END OF LIST...')
    return



def add_test(user):
    print('Adding New Test')
    while True:
        try:
            name = input('Enter test name: ').strip().capitalize()
            if name == '':
                raise ValueError('Test name cannot be empty. Try again...')
            else:
                break
        except ValueError as e:
            print(e)

    for k,v in data.items():
        if v['test name'] == name:
            print('Test alredy exists with Test ID:',k)
            return

    while True:
        try:
            low = input('Enter test low range: ').strip()
            if low == '':
                raise ValueError('Value cannot be empty. Try again...')
            elif not low.isdigit():
                raise ValueError('Enter number only...')
            else:
                low = int(low)
                break
        except ValueError as e:
            print(e)

    while True:
        try:
            high = input('Enter test high range: ').strip()
            if high == '':
                raise ValueError('Value cannot be empty. Try again...')
            elif not high.isdigit():
                raise ValueError('Enter number only...')
            else:
                high = int(high)
                break
        except ValueError as e:
            print(e)
        
    while True:
        try:
            unit = input('Enter no of unit: ').strip()
            if unit == '':
                raise ValueError('Unit cannot be empty. Try again...')
            elif not unit.isdigit():
                raise ValueError('Enter number only...')
            else:
                unit = int(unit)
                break
        except ValueError as e:
            print(e)

    while True:
        try:
            price = input('Enter Price in Rs: ').strip()
            if price == '':
                raise ValueError('Price cannot be empty. Try again...')
            elif not price.isdigit():
                raise ValueError('Enter number only...')
            else:
                price = int(price)
                break
        except ValueError as e:
            print(e)


    if not data:
        new_id = 101
    else:
        new_id = next(reversed(data)) + 1
    data[new_id] = {'test name': name, 'low range': low, 'high range': high, 'unit':unit , 'price':price, 'is_active': True}

    print('Successfully Added with test ID: ',new_id)
    message = f"New Test with ID-{new_id} was added by Lab Technician-{user}"
    add_logs(message)


def manage_test_menu(user):
    while True:
        print('\n\t\t CMS Manage Lab Menu')
        print('\t\t************************')
        print('\t\tWelcome ',user)
        print('''What would you like to do?
                1. Add test
                2. View list of test
                3. Search and View test
                4. Logout''')
        try:
            ch = input('Enter your choice: ').strip()
            if not ch.isdigit():
                raise ValueError('Please enter a number')
            else:
                match int(ch):
                    case 1:
                        add_test(user)
                    case 2:
                        list_test()
                    case 3:
                        search_menu()    
                    case 4:
                        print('Logging out....\n')
                        return
                    case _:
                        print('Enter a valid number')
        except ValueError as e:
            print(e)
            