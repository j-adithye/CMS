from validation import validate_username,validate_pwd
from patient.menu import receptionist_menu
from data import employee_data
from staff.staff_manager import manage_staff_menu
from lab.lab_manager import manage_test_menu
from medicine.medicine_manager import manage_medicine_menu
from logs.log_manager import add_logs
import sys

def main():
    print('\t\t Welcome to CMS')
    print('\t\t  Plese Login')
    print('\t\t*****************')
    i = 0
    while i<4:
            if i == 3:
                print('3 Invalid login attempts \nPlease try after Sometime\n')
                #add to log file here
                print('Updating log file...\n')
                message = f"3 consecutive login fails. last used username='{user}'"
                add_logs(message)

                print('Application closing...')
                sys.exit()

            try:
                while True:
                    try:
                        user = input('Enter User Name: ').lower().strip() #username input
                        if user == '':
                            raise ValueError('Username cannot be empty\n') #empty username validation
                        if validate_username(user):
                            break
                        else:
                            raise ValueError('Username cannot be shorter than 6 characters')
                    except ValueError as e:
                         print(e)
                while True:
                    try:
                        pwd = input('Enter Password: ').strip()
                        if pwd == '':
                            raise ValueError('Password cannot be empty\n')
                        if validate_pwd(pwd):
                            break
                        else:
                            raise ValueError('Password cannot be shorter than 6 char')
                    except ValueError as e:
                         print(e)
                if employee_data.get(user) != None:
                     if employee_data.get(user).get('password') == pwd:
                        if employee_data.get(user).get('role') == 'receptionist':
                            receptionist_menu(user)

                        elif employee_data.get(user).get('role') == 'admin':
                            manage_staff_menu(user)

                        elif employee_data.get(user).get('role') == 'pharmacist':
                            manage_medicine_menu(user)

                        elif employee_data.get(user).get('role') == 'lab technician':
                            manage_test_menu(user)

                        else:
                            print(f'Login attempt {i+1} failed\n')
                            i += 1
                            raise Exception('You are not a Registered Employee')
                     else:
                        print(f'Login attempt {i+1} failed\n')
                        i += 1
                        raise ValueError('Username or Password Incorrect\n')
                        
                else:
                    print(f'Login attempt {i+1} failed\n')
                    i += 1
                    raise ValueError('Username or Password Incorrect\n')
            except Exception as e:
                print(e)
            


if __name__ == "__main__":
    main()
