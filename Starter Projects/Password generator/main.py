import string
import secrets
# This function is part of the secrets module,
# which provides functions for generating secure random numbers


# three functions - contains_upper, contains_symbol, genereate_password

def contains_upper(password: str) -> bool:
    #This function checks whether the password contains uppercase or not

    for char in password:
        if char.isupper():
            return True

    return False

def contains_symbol(password: str) -> bool:
    #This function checks whether the password contains symobols or not

    for char in password:
        if char in string.punctuation:
            return True

    return False

def generate_password(length: int, symbols: bool, uppercase: bool ) -> str:
    # This function generates the password
    # param1 - length - length og the password
    # param2 - symbol - whether the password should contains symbol or not
    # param3 - uppercase - whether the password should contains uppercase or not

    #create a combination of characters to choose from
    # if we need symbols in the password then

    combination:str = ''
    if symbols:
        combination += string.punctuation

    # if we need uppercase letters in the password then
    if uppercase:
        combination += string.ascii_uppercase

    combination += string.ascii_lowercase + string.digits

    # length of the combination string
    combination_length: int = len(combination)

    #generate a new_password
    new_password: str = ''

    # append a new secret random char to the new_password
    for i in range(length):

        if symbols:
            sym: str = combination[secrets.randbelow(combination_length)]
            while sym not in string.punctuation:
                sym = combination[secrets.randbelow(combination_length)]
                continue
            new_password += sym
            i+=1
            symbols = False
            continue

        if uppercase:
            upper: str = combination[secrets.randbelow(combination_length)]
            while upper not in string.ascii_uppercase:
                upper = combination[secrets.randbelow(combination_length)]
                continue
            new_password += upper
            i+=1
            uppercase = False
            continue

        new_password+= combination[secrets.randbelow(combination_length)]

    # now, return the new_password as the final output
    return new_password


if __name__ == '__main__':

    #generating 5 strong passwords
    for i in range(1,6):
        new_pass: str = generate_password(length=2, symbols= True, uppercase= True)
        specs: str = f'U: {contains_upper(new_pass)}, S: {contains_symbol(new_pass)}'
        print(f'{i} -> {new_pass} ({specs})')

