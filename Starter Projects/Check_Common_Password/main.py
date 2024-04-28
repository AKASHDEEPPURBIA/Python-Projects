def check_password(password: str):

    if(len(password)<8):
        print(f'{password}: ❌')
        return

    #open up the file with most common passwords and closing again after reading all
    #That's why we have used with
    #storing all values in the list[str]
    with open('password.txt', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

    for i, common_password in enumerate(common_passwords):
        if password == common_password:
            print(f'{password}: ❌')
            return

    print(f'{password}: ✔ (Unique)')

def main():
    user_password: str = input('Enter a password: ')
    check_password(user_password)

if __name__ == '__main__':
    main()
