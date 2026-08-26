from validation import validate_name,validate_phone,validate_date
from data import medicine_data as data
from medicine.search_and_edit_medicine import search_menu
from logs.log_manager import add_logs


def list_medicine():
    print('Medicine ID\t Medicine name\t Company name\t\t Generic name\t\t Quantity\t Price\t Is Active')
    for k,v in data.items():
        print(f'{k}\t\t {v['medicine name']}\t {v['company name']}\t {v['generic name']}\t\t {v['quantity']}\t\t {v['price']}\t {v['is_active']}')

    print('END OF LIST...')
    return



def add_medicine(user):
    print('Adding New Medicine')
    while True:
        try:
            name = input('Enter medicine name: ').strip().capitalize()
            if name == '':
                raise ValueError('Medicine name cannot be empty. Try again...')
            else:
                break
        except ValueError as e:
            print(e)

    while True:
        try:
            cmpny_name = input('Enter company name: ').strip().capitalize()
            if name == '':
                raise ValueError('Company name cannot be empty. Try again...')
            else:
                break
        except ValueError as e:
            print(e)

    for k,v in data.items():
        if v['company name'] == cmpny_name and v['medicine name'] == name:
            print('Medicine alredy exists with Medicine ID:',k)
            return

    while True:
        try:
            gen_name = input('Enter generic name: ').strip().capitalize()
            if name == '':
                raise ValueError('Generic name cannot be empty. Try again...')
            else:
                break
        except ValueError as e:
            print(e)

    while True:
        try:
            qty = input('Enter Quantity in no of units: ').strip()
            if qty == '':
                raise ValueError('Quantity cannot be empty. Try again...')
            elif not qty.isdigit():
                raise ValueError('Enter number only...')
            else:
                qty = int(qty)
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
    data[new_id] = {'medicine name': name, 'company name': cmpny_name , 'generic name': gen_name , 'quantity':qty, 'price':price , 'is_active': True}

    print('Successfully Added with Medicine ID: ',new_id)
    message = f"New Medicine with ID-{new_id} was added by Pharmacist-{user}"
    add_logs(message)


def manage_medicine_menu(user):
    while True:
        print('\n\t\t CMS Manage Pharmacy Menu')
        print('\t\t************************')
        print('\t\tWelcome ',user)
        print('''What would you like to do?
                1. Add Medicine
                2. View list of Medicine
                3. Search and View Medicine
                4. Logout''')
        try:
            ch = input('Enter your choice: ').strip()
            if not ch.isdigit():
                raise ValueError('Please enter a number')
            else:
                match int(ch):
                    case 1:
                        add_medicine(user)
                    case 2:
                        list_medicine()
                    case 3:
                        search_menu()    
                    case 4:
                        print('Logging out....\n')
                        return
                    case _:
                        print('Enter a valid number')
        except ValueError as e:
            print(e)
            