from patient_manager import manage_patients_menu
from log_manager import view_logs
import sys


def menu(user):
    print('\n\t\t Clinic Management System')
    print('\t\t************************')
    print('\t\t   Welcome ',user)
    print('''What would you like to do?
            1. Manage Patients
            2. View logs
            3. Logout and Exit''')
    while True:
        try:
            ch = input('Enter your choice: ').strip()
            if not ch.isdigit():
                raise ValueError('Please enter a number')
            else:
                match int(ch):
                    case 1:
                        manage_patients_menu()
                    case 2:
                        view_logs()
                    case 3:
                        print('logging out...')
                        print('Exiting...')
                        sys.exit()
                    case _:
                        print('Enter a valid number')
        except ValueError as e:
            print(e)