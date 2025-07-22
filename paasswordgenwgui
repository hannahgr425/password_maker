import random
import string
import datetime
from tkinter import *
from tkinter import font
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
