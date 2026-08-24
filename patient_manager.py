from menu import menu


patients_data = {}


def add_patient():
    pass

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