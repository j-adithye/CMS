from validation import validate_username,validate_pwd
from menu import menu

users = {'a':{'password':'a','role':'admin'},'arun':{'password':'Arun@123','role':'admin'}, 'roshin':{'password':'Roshin@123','role':'admin'}, 'albin': {'password':'albin@123','role':'admin'}}

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
                        user = input('Enter User Name: ').lower() #username input
                        if user == '':
                            raise ValueError('Username cannot be empty\n') #empty username validation
                        if validate_username(user):
                             break
                    except ValueError as e:
                         print(e)
                while True:
                    try:
                        pwd = input('Enter Password: ')
                        if pwd == '':
                            raise ValueError('Password cannot be empty\n')
                        else:
                             break
                    except ValueError as e:
                         print(e)
                if users.get(user) != None:
                     if users.get(user).get('password') == pwd:
                        if users.get(user).get('role') == 'admin':
                            menu(user)
                        else:
                            print(f'Login attempt {i+1} failed\n')
                            raise Exception('User is not an Admin')
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
