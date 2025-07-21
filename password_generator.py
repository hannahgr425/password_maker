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
while generate not in ["y", "n"]:
    print("please enter Y or N")
    generate=input("would you like to generate a new password? Y/N: ").lower()
while generate== "y":
    print("Password choices:\n" \
    "1. lower case\n" \
    "2. upper case\n" \
    "3. symbols\n" \
    "4. numbers\n" \
    "-----------------------------------\nfor all options please enter Y or N if you want to include that option\n")
    toggle_input=False
    while toggle_input ==False:
        choice_lower= input("lower case: ").lower()
        while choice_lower not in ["y", "n"]:
            print("please enter Y or N")
            choice_lower= input("lower case: ").lower()
        choice_upper= input("upper case: ").lower()
        while choice_upper not in ["y", "n"]:
            print("please enter Y or N")
            choice_upper= input("upper case: ").lower()
        choice_symbols= input("symbols: ").lower()
        while choice_symbols not in ["y", "n"]:
            print("please enter Y or N")
            choice_symbols= input("symbols: ").lower()
        choice_numbers= input("numbers: ").lower()
        while choice_numbers not in ["y", "n"]:
            print("please enter Y or N")
            choice_numbers= input("numbers:").lower()
        valid_length=False
        while not valid_length:
            try:
                password_length=int(input("\n\npassword length: "))
            except ValueError:
                print("please enter an integer greater than one.")
                password_length=int(input("\npassword length: "))
            else:
                valid_length=True
        choices = [choice_lower, choice_upper, choice_symbols, choice_numbers]
        print ("\n--------------------------------------\n\nYou have chosen: \n"\
               f"lower case: {choice_lower}\n"\
                f"upper case: {choice_upper}\n"\
                f"symbols: {choice_symbols}\n"\
                f"numbers: {choice_numbers}\n"
                f"password length: {password_length}\n")
        change=input("are you happy with your choices? Y/N ").lower()
        while change not in ["y", "n"]:
            print("please enter Y or N")
            change=input("are you happy with your choices? Y/N: ").lower()
        while change == "n":
            choice_lower= input("lower case: ").lower()
            while choice_lower not in ["y", "n"]:
                print("please enter Y or N")
                choice_lower= input("lower case: ").lower()
            choice_upper= input("upper case: ").lower()
            while choice_upper not in ["y", "n"]:
                print("please enter Y or N")
                choice_upper= input("upper case: ").lower()
            choice_symbols= input("symbols: ").lower()
            while choice_symbols not in ["y", "n"]:
                print("please enter Y or N")
                choice_symbols= input("symbols: ").lower()
            choice_numbers= input("numbers: ").lower()
            while choice_numbers not in ["y", "n"]:
                print("please enter Y or N")
                choice_numbers= input("numbers: ").lower()
            valid_length=False
            while not valid_length:
                try:
                    password_length=int(input("\n\npassword length: "))
                except ValueError:
                    print("please enter an integer greater than one.")
                    password_length=int(input("\npassword length: "))
                else:
                    valid_length=True
            print ("you have chosen: \n"\
               f"lower case: {choice_lower}\n"\
                f"upper case: {choice_upper}\n"\
                f"symbols: {choice_symbols}\n"\
                f"numbers: {choice_numbers}\n"\
                f"password length: {password_length}\n")
            choice=input("are you happy with your choices? Y/N ").lower()
        if change == "y":
            toggle_input=True
    generate_password = generate_password()
    print("\n\nGenerated password: ",generate_password)
    generate=input("\nwould you like to generate a new password? Y/N: ").lower()