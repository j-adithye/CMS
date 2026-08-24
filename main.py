from validation import validate_username,validate_pwd
from menu import menu

users = {'arun':'Arun@123', 'roshin':'Roshin@123', 'albin': 'AlibinP@123'}

def main():
    print('\t\t Welcome to CMS')
    print('\t\t  Plese Login')
    print('\t\t*****************')

    while True:
        try:
            user = input('Enter User Name: ').lower()
            if user == '':
                raise ValueError('Username cannot be empty\n')
            elif users.get(user) == None:
                raise ValueError('User does not Exist\n')
            else:
                 break
        except ValueError as e:
            print(e)

    for i in range(4):
            if i == 3:
                print('3 Invalid login attempts \nPlease try after Sometime\n')
                #add to log file here

                break

            try:
                pwd = input('Enter Password: ')
                if pwd == '':
                    raise ValueError('Password cannot be empty\n')
                elif pwd == users[user]:
                        menu(user)
                else:
                    print(f'Login attempt {i+1} failed\n')
                    raise ValueError('Incorrect Password\n')
            except ValueError as e:
                print(e)
            


if __name__ == "__main__":
    main()
