from validation import validate_username,validate_pwd
from menu import staff_menu
from data import employee_data
from staff.staff_manager import manage_staff_menu

def main():
    print('\t\t Welcome to CMS')
    print('\t\t  Plese Login')
    print('\t\t*****************')

    for i in range(4):
            if i == 3:
                print('3 Invalid login attempts \nPlease try after Sometime\n')
                #add to log file here

                break

            try:
                while True:
                    try:
                        user = input('Enter User Name: ').lower().strip() #username input
                        if user == '':
                            raise ValueError('Username cannot be empty\n') #empty username validation
                        if validate_username(user):
                             break
                    except ValueError as e:
                         print(e)
                while True:
                    try:
                        pwd = input('Enter Password: ').strip()
                        if pwd == '':
                            raise ValueError('Password cannot be empty\n')
                        else:
                             break
                    except ValueError as e:
                         print(e)
                if employee_data.get(user) != None:
                     if employee_data.get(user).get('password') == pwd:
                        if employee_data.get(user).get('role') == 'staff':
                            staff_menu(user)
                        elif employee_data.get(user).get('role') == 'admin':
                            manage_staff_menu(user)
                        elif employee_data.get(user).get('role') == 'pharmacist':
                            manage_staff_menu(user)
                        else:
                            print(f'Login attempt {i+1} failed\n')
                            raise Exception('You are not a staff')
                     else:
                        print(f'Login attempt {i+1} failed\n')
                        raise ValueError('Username or Password Incorrect\n')
                        
                else:
                    print(f'Login attempt {i+1} failed\n')
                    raise ValueError('Username or Password Incorrect\n')
            except Exception as e:
                print(e)
            


if __name__ == "__main__":
    main()
