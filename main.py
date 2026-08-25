from validation import validate_username,validate_pwd
from menu import menu
from data import staff_data

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
                if staff_data.get(user) != None:
                     if staff_data.get(user).get('password') == pwd:
                        if staff_data.get(user).get('role') == 'staff':
                            menu(user)
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
