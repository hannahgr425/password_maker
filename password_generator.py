import random
import string

def lowercase():
    random_lower=random.choice(string.ascii_lowercase)
    return random_lower

def uppercase():
    random_upper=random.choice(string.ascii_uppercase)
    return random_upper

def symbols():
    random_symbol=random.choice(string.punctuation)
    return random_symbol

def numbers():
    random_number=random.choice(string.digits)
    return random_number

def generate_password():
    password=[]
    randint_limit=password_length
    while randint_limit > 0:
        if choice_lower == "y":
            limit=random.randint(0,(randint_limit//2)+1)
            for i in range(0, limit):
                password.append(lowercase())
            randint_limit -= limit
        if choice_upper == "y":
            limit=random.randint(0,(randint_limit//2)+1)
            for i in range(0, limit):
                password.append(uppercase())
            randint_limit -= limit
        if choice_symbols == "y":
            limit=random.randint(0,(randint_limit//2)+1)
            for i in range(0, limit):
                password.append(symbols())
            randint_limit -= limit
        if choice_numbers == "y":
            limit=random.randint(0,(randint_limit//2)+1)
            for i in range(0, limit):
                password.append(numbers())
            randint_limit -= limit
    random.shuffle(password)
    return ''.join(password)


print("Welcome to the password generator")
generate=input("would you like to generate a new password? Y/N: ").lower()
while generate== "y":
    print("password choices" \
    "1. lower case" \
    "2. upper case" \
    "3. symbols" \
    "4. numbers")
    toggle_input=False
    while toggle_input ==False:
        choice_lower= input("lower case: Y/N: ").lower()
        choice_upper= input("upper case: Y/N: ").lower()
        choice_symbols= input("symbols: Y/N: ").lower()
        choice_numbers= input("numbers: Y/N: ").lower()
        choices = [choice_lower, choice_upper, choice_symbols, choice_numbers]
        change=input("are you happy with your choices? Y/N: ").lower()
        while change not in ["y", "n"]:
            print("please enter Y or N")
        while change == "n":
            choice_lower= input("lower case: Y/N: ").lower()
            choice_upper= input("upper case: Y/N: ").lower()
            choice_symbols= input("symbols: Y/N: ").lower()
            choice_numbers= input("numbers: Y/N: ").lower()
 
        while change == "n":
            choice=input("are you happy with your choices? Y/N: ").lower()
        if change == "y":
            toggle_input=True
    password_length=int(input("password length: "))
    generate_password = generate_password()
    print("generated password: ",generate_password)
    generate=input("would you like to generate a new password? Y/N: ").lower()