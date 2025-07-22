import random
import string
import datetime
from tkinter import *
from tkinter import font



"""class password():
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.symbols = string.punctuation
        self.numbers = string.digits
        self.choice_lower = ""
        self.choice_upper =""
        self.choice_symbols =""
        self.choice_numbers = ""
        self.password_length = 0
        self.password = ""
        
    def get_choice_lower(self):
        return self.choice_lower
    def get_choice_upper(self):
        return self.choice_upper
    def get_choice_symbols(self):
        return self.choice_symbols
    def get_choice_numbers(self):
        return self.choice_numbers
    def get_password_length(self):
        return self.password_length
    def get_password(self):
        return self.password
        

    def set_choice_lower(self, choice_lower):
        self.choice_lower = choice_lower
    def set_choice_upper(self, uppercase):
        self.choice_upper=uppercase
    def set_choice_symbols(self, symbols):
        self.choice_symbols=symbols
    def set_choice_numbers(self, numbers):
        self.choice_numbers = numbers
    def set_password_length(self, length):
        self.password_length = length
    def set_password(self,password):
        self.password = password

    def random_lower(self):
        random_lower = random.choice(self.lowercase)
        return random_lower
    def random_upper(self):
        random_upper = random.choice(self.uppercase)
        return random_upper
    def random_symbol(self):
        random_symbol = random.choice(self.symbols)
        return random_symbol
    def random_numbers(self):
        random_number = random.choice(self.numbers)
        return random_number
        
    def change_lower(self):
        choice_lower = input("Include lowercase letters? (y/n): ").lower()
        while choice_lower not in ["y","n"]:
            print("Please enter y/n")
            choice_lower =  input("Include lowercase letters? (y/n): ").lower()
        self.set_choice_lower(choice_lower)
    def change_upper(self):
        choice_upper = input("Include uppercase letters? (y/n): ").lower()
        while choice_upper not in ["y","n"]:
            print("Please enter y/n")
            choice_upper =  input("Include uppercase letters? (y/n): ").lower()
        self.set_choice_upper(choice_upper)
    def change_symbols(self):
        choice_symbol = input("Include symbols? (y/n): ").lower()
        while choice_symbol not in ["y","n"]:
            print("Please enter y/n")
            choice_symbol =  input("Include symbols? (y/n): ").lower()
        self.set_choice_symbols(choice_symbol)
    def change_numbers(self):
        choice_number = input("Include numbers? (y/n): ").lower()
        while choice_number not in ["y","n"]:
            print("Please enter y/n")
            choice_number =  input("Include numbers? (y/n): ").lower()
        self.set_choice_numbers(choice_number)

    def change_password_length(self):
        valid_length = False
        while not valid_length:
            try:
                password_length = int(input("Enter the desired password length (minimum 1): "))
            except ValueError:
                print("Please enter a valid integer greater than zero.")  
            else:
                self.set_password_length(password_length)     
                valid_length = True

    def generate_password(self):
        password=[]
        randint_limit=self.get_password_length()
        while randint_limit > 0:
            if self.get_lowervar() == 1:
                limit=random.randint(0,(randint_limit//2)+1)
                for i in range(0, limit):
                    password.append(self.random_lower())
                randint_limit -= limit
            if self.get_uppervar()==1:
                limit=random.randint(0,(randint_limit//2)+1)
                for i in range(0, limit):
                    password.append(self.random_upper())
                randint_limit -= limit
            if self.get_symbolsvar()==1:
                limit=random.randint(0,(randint_limit//2)+1)
                for i in range(0, limit):
                    password.append(self.random_symbol())
                randint_limit -= limit
            if self.get_numbersvar()==1:
                limit=random.randint(0,(randint_limit//2)+1)
                for i in range(0, limit):
                    password.append(self.random_numbers())
                randint_limit -= limit
            random.shuffle(password)
            self.set_password(''.join(password))

    def display_password(self):
        print("\nGenerated password: ", self.get_password())

    def welcome_message():
        print("Welcome to the password generator\n" \
                "This program will help you create a secure password.\n" \
                "You can choose to include lowercase letters, uppercase letters, symbols, and numbers. \n" \
                "You can also specify the length of the password. \n" \
                "Lets get started!\n")

    def display_choices(self):
        print("\n--------------------------------------\n\nYou have chosen: \n" \
            "lower case: ", self.get_choice_lower(),"\n"\
            "upper case: ", self.get_choice_upper(),"\n"\
            "symbols: ", self.get_choice_symbols(),"\n"\
            "numbers: ",self.get_choice_numbers(),"\n"
            "password length: ",self.get_password_length(),"\n")   """
        


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.lowerVar = IntVar()
        self.upperVar = IntVar()
        self.symbolsVar = IntVar()
        self.numbersVar = IntVar()
        self.password_length=IntVar()

        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.symbols = string.punctuation
        self.numbers = string.digits
        self.password = ""
        

        exit_button = Button(self, text="Exit", command=self.ClickExit)
        exit_button.place(x=0, y=0)

    def random_lower(self):
        random_lower = random.choice(self.lowercase)
        return random_lower
    def random_upper(self):
        random_upper = random.choice(self.uppercase)
        return random_upper
    def random_symbol(self):
        random_symbol = random.choice(self.symbols)
        return random_symbol
    def random_numbers(self):
        random_number = random.choice(self.numbers)
        return random_number
    
    def set_password(self,password):
        self.password = password
    def get_password(self):
        return self.password

    def welcome_message(self):
        welcome_label = Label(self, text="Welcome to the Password Generator", bg="lightsteelblue", font=("Helvetica", 16))
        welcome_label.pack(pady=15)
    def ClickExit(self):
        exit()
    
    def checkbutton(self):
        check_label = Label(self, text="Select Password Options", bg="lightsteelblue", font=("Helvetica", 14))
        check_label.pack(padx=5, pady=10)
        lowercase = Checkbutton(root, text = "Lowercase", font=("Helvetica", 12), onvalue = 1 , offvalue = 0, variable = self.lowerVar, relief = "groove", activebackground= "steelblue", activeforeground = "pale turquoise", bg="lightsteelblue")
        lowercase.pack(after=check_label, padx=5, pady=5)
        uppercase = Checkbutton(root, text = "Uppercase", font=("Helvetica", 12), onvalue = 1 , offvalue = 0, variable = self.upperVar, relief = "groove", activebackground="steelblue", activeforeground = "pale turquoise", bg="lightsteelblue")
        uppercase.pack(after=lowercase, padx=5, pady=5)
        symbols = Checkbutton(root, text = "Symbols", font=("Helvetica", 12), onvalue = 1 , offvalue = 0, variable = self.symbolsVar, relief = "groove", activebackground="steelblue", activeforeground = "pale turquoise", bg="lightsteelblue")
        symbols.pack(after=uppercase, padx=5, pady=5)
        numbers = Checkbutton(root, text = "Numbers", font=("Helvetica", 12), onvalue = 1 , offvalue = 0, variable = self.numbersVar , relief = "groove", activebackground="steelblue", activeforeground = "pale turquoise", bg="lightsteelblue")
        numbers.pack(after=symbols, padx=5, pady=5)


    def entry_space(self):
        length_entry=""
        input_title=Label(self, text="Please input password length:", bg="lightsteelblue", font=("Helvetica",12))
        input_title.place(x=830, y=300)
        length_entry=Entry(self, textvariable=self.password_length ,width=8)
        length_entry.place(x=1050, y=300)
        """if length_entry!="":
            try:
                user_input= self.password_length.get()
            except ValueError:
                print("Error","Please enter a valid integer")
            else:
                self.password_length=user_input"""

       

    def generate_button(self):
        generate_button = Button(self,text="Generate Password", font=("Helvetica", 12),bg="lightsteelblue", activebackground="azure", activeforeground="white", command=self.generate_password)
        #command=password().generate_password # could get commmand to take an objext or make generate_password a static method
        generate_button.place(x=875, y=400)

    def get_lowervar(self):
        return self.lowerVar.get()
    def get_uppervar(self):
        return self.upperVar.get()
    def get_symbolsvar(self):
        return self.symbolsVar.get()
    def get_numbersvar(self):
        return self.numbersVar.get()
    def get_passwordlength(self):
        return self.password_length.get()
    
    def generate_password(self):
        password=[]
        randint_limit=self.get_passwordlength()
        while randint_limit > 0:
            if self.get_lowervar() == 1:
                limit=random.randint(0,(randint_limit//2)+1)
                for i in range(0, limit):
                    password.append(self.random_lower())
                randint_limit -= limit
            if self.get_uppervar()==1:
                limit=random.randint(0,(randint_limit//2)+1)
                for i in range(0, limit):
                    password.append(self.random_upper())
                randint_limit -= limit
            if self.get_symbolsvar()==1:
                limit=random.randint(0,(randint_limit//2)+1)
                for i in range(0, limit):
                    password.append(self.random_symbol())
                randint_limit -= limit
            if self.get_numbersvar()==1:
                limit=random.randint(0,(randint_limit//2)+1)
                for i in range(0, limit):
                    password.append(self.random_numbers())
                randint_limit -= limit
            random.shuffle(password)
            self.set_password(''.join(password))
            self.display_password()
    def display_password(self):
        password_label=Label(self, text=f"Your random password is: {self.get_password()}", bg="lightsteelblue", font=("Helvetica",12))
        password_label.place(x=800, y=500)
    
    def save_button(self):
        save_button = Button(self,text="Save Password", font=("Helvetica", 10),bg="lightsteelblue", activebackground="azure", activeforeground="white", command=self.savetofile)
        #command=password().generate_password # could get commmand to take an objext or make generate_password a static method
        save_button.place(x=600, y=600)

    def savetofile(self):
        from datetime import datetime

        with open("saved_passwords.txt", "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d_%H.%M.%S")+"  "+self.get_password()+"\n")
    
    def erase_button(self):
        erase_button = Button(self,text="Erase Password", font=("Helvetica", 10),bg="lightsteelblue", activebackground="azure", activeforeground="white", command=self.erasefile)
        #command=password().generate_password # could get commmand to take an objext or make generate_password a static method
        erase_button.place(x=1100, y=600)

    def erasefile(self):
        with open("saved_passwords.txt", "w") as file:
            file.write("")
        


root = Tk()
app = Window(root)
root.geometry("400x300")
app.configure(bg="lightsteelblue")
root.wm_title("Password Generator")
app.welcome_message()
app.checkbutton()
app.entry_space()
app.generate_button()
app.save_button()
app.erase_button()
root.mainloop()

"""password_instance = password(app)
generate = input("Would you like to generate a new password? Y/N: ").lower()
while generate not in ["y","n"]:
    print("Please enter Y or N")
    generate = input("Would you like to generate a new password? Y/N:").lower()
while generate == "y":
    password_instance.welcome_message
    password_instance.change_lower()
    password_instance.change_upper()
    password_instance.change_symbols()
    password_instance.change_numbers()
    password_instance.change_password_length()
    password_instance.display_choices()
    while password_instance.get_choice_lower()=="n" and password_instance.get_choice_upper()=="n" and password_instance.get_choice_symbols()=="n" and password_instance.get_choice_numbers()=="n":
        print("you must choose at least one option to generate a password")
        to_change = input("What would you like to change? (1. lower/2. upper/3. symbols/4. numbers):").lower()
        if to_change == "1":
            password_instance.change_lower()
        elif to_change == "2":
            password_instance.change_upper()
        elif to_change =="3":
            password_instance.change_symbols()
        elif to_change == "4":
            password_instance.change_numbers()
    change = input("Are you happy with your choices? Y/N: ").lower()
    while change not in ["y", "n"]:
        print("Please enter Y or N")
        change = input("Are you happy with your choices? Y/N:").lower()
    while change == "n":
        to_change = input("What would you like to change? (1. lower/2. upper/3. symbols/4. numbers/5. password length):").lower()
        if to_change == "1":
            password_instance.change_lower()
        elif to_change == "2":
            password_instance.change_upper()
        elif to_change =="3":
            password_instance.change_symbols()
        elif to_change == "4":
            password_instance.change_numbers()
        elif to_change == "5":
            password_instance.change_password_length()
        else:
            print("Invalid choice, please try again.")
        password_instance.display_choices()
        change = input("Are you happy with your choices? Y/N: ").lower()
    password_instance.generate_password()
    password_instance.display_password()
    save_password = input("Would you like to save this password? Y/N: ").lower()
    while save_password not in ["y", "n"]:
        print("Please enter Y or N")
        save_password = input("Would you like to save this password? Y/N: ").lower()
    if save_password == "y":
        from datetime import datetime

        with open("saved_passwords.txt", "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d_%H.%M.%S")+"  "+password_instance.get_password()+"\n")
    generate = input("\nWould you like to generate a new password? Y/N: ").lower()
    while generate not in ["y","n"]:
        print("Please enter Y or N")
        generate = input("Would you like to generate a new password? Y/N:").lower()
if generate == "n":
    delete_password = input("Would you like to delete the saved passwords? Y/N: ").lower()
    while delete_password not in ["y", "n"]:
        print("Please enter Y or N")
        delete_password = input("Would you like to delete the saved passwords? Y/N: ").lower()
    if delete_password == "y":
        with open("saved_passwords.txt", "w") as file:
            file.write("")"""









"""def lowercase():
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
    return ''.join(password)"""


"""print("Welcome to the password generator")
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
    generate=input("\nwould you like to generate a new password? Y/N: ").lower()"""