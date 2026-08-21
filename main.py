from validation import validate_username,validate_pwd

users = {'arun':'Arun@123', 'roshin':'Roshin@123', 'albin': 'AlibinP@123'}

def main():
    print('\t\t Welcome to CMS')
    print('\t\t Plese Login')
    print('\t\t*******************')

    while True:
        try:
            user = input('Enter User Name: ').lower()
            if user == '':
                raise ValueError('Username cannot be empty')
            elif validate_username(user):
                if user in users.keys():
                    break
                else:
                    raise ValueError('User does not Exist')
            else:
                raise ValueError('Username should only contain letters and numbers')
        except ValueError as e:
            print(e)

    while True:
            try:
                pwd = input('Enter Password: ')
                if pwd == '':
                    raise ValueError('Password cannot be empty')
                elif validate_pwd(user):
                    if pwd == users[user]:
                        break
                    else:
                        raise ValueError('Incorrect Password')
                else:
                    raise ValueError('Invalid Password')
            except ValueError as e:
                print(e)
            


if __name__ == "__main__":
    main()
