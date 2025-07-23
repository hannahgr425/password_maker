import random
import string
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
        self.error_msg=Label(self, text="", foreground="steelblue", bg="lightsteelblue", font=("Consolas",12))
        self.error_msg.place(x=810, y=800)

        #error_msg1=Label(self, text="invalid password length!", foreground="steelblue", bg="lightsteelblue", font=("Consolas",12))
        try:
            self.password_length=IntVar()
        except:
            self.error_msg.configure(text="invalid password length!", foreground="steelblue")
            return
        

        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.symbols = string.punctuation
        self.numbers = string.digits
        self.password = ""
        self.password_change= StringVar()
        

        exit_button = Button(self, text="Exit", command=self.ClickExit)
        exit_button.place(x=0, y=0)

        """self.error_msg1=Label(self, text="", foreground="steelblue", bg="lightsteelblue", font=("Consolas",12))
        self.error_msg1.place(x=810, y=800)
        self.error_msg2=Label(self, text="", foreground="steelblue", bg="lightsteelblue", font=("Consolas",12))
        self.error_msg1.place(x=810, y=800)"""

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
        welcome_label = Label(self, text="Welcome to the Password Generator!", bg="lightsteelblue", font=("Courier", 40))
        welcome_label.pack(pady=15)
    def ClickExit(self):
        exit()
    
    def checkbutton(self):
        check_label = Label(self, text="Select Password Options:", bg="lightsteelblue", font=("Consolas", 20))
        check_label.pack(padx=5, pady=10)
        lowercase = Checkbutton(root, text = "LOWERCASE", font=("Consolas", 12), onvalue = 1 , offvalue = 0, variable = self.lowerVar, relief = "groove", activebackground= "steelblue", activeforeground = "pale turquoise", bg="lightsteelblue")
        lowercase.place(x=600, y=175)
        uppercase = Checkbutton(root, text = "UPPERCASE", font=("Consolas", 12), onvalue = 1 , offvalue = 0, variable = self.upperVar, relief = "groove", activebackground="steelblue", activeforeground = "pale turquoise", bg="lightsteelblue")
        uppercase.place(x=800, y=175)
        symbols = Checkbutton(root, text = "SYMBOLS", font=("Consolas", 12), onvalue = 1 , offvalue = 0, variable = self.symbolsVar, relief = "groove", activebackground="steelblue", activeforeground = "pale turquoise", bg="lightsteelblue")
        symbols.place(x=1000, y=175)
        numbers = Checkbutton(root, text = "NUMBERS", font=("Consolas", 12), onvalue = 1 , offvalue = 0, variable = self.numbersVar , relief = "groove", activebackground="steelblue", activeforeground = "pale turquoise", bg="lightsteelblue")
        numbers.place(x=1200, y=175)


    def entry_space(self):
        length_entry=""
        input_title=Label(self, text="Please input password length:", bg="lightsteelblue", font=("Consolas",12))
        input_title.place(x=790, y=250)
        length_entry=Entry(self, textvariable=self.password_length ,width=8)
        length_entry.place(x=1060, y=252)
        """if length_entry!="":
            try:
                user_input= self.password_length.get()
            except ValueError:
                print("Error","Please enter a valid integer")
            else:
                self.password_length=user_input"""

    """def place_errormsg2(self, to_do):
        error_msg2=Label(self, text="Please select password options!", foreground="steelblue", bg="lightsteelblue", font=("Consolas",12))
        if to_do==True:
            error_msg2.place_configure(x=810, y=800)
        elif to_do==False:
            error_msg2.place_forget()"""
        
    def generate_button(self):
        generate_button = Button(self,text="Generate Password", font=("Consolas", 15),bg="lightsteelblue", activebackground="steelblue", activeforeground="pale turquoise", command=self.generate_password)
        #command=password().generate_password # could get commmand to take an objext or make generate_password a static method
        generate_button.place(x=860, y=320)
    
   
    def get_lowervar(self):
        return self.lowerVar.get()
    def get_uppervar(self):
        return self.upperVar.get()
    def get_symbolsvar(self):
        return self.symbolsVar.get()
    def get_numbersvar(self):
        return self.numbersVar.get()
    def get_passwordlength(self):
        #error_msg1=Label(self, text="invalid password length!", foreground="steelblue", bg="lightsteelblue",font=("Consolas",12))
        try:
            return self.password_length.get()
        except:
            self.error_msg.configure(text="invalid password length!", foreground="steelblue")


        
    
    def generate_password(self):
        password=[]
        #error_msg1=Label(self, text="invalid password length!", foreground="steelblue", bg="lightsteelblue", font=("Consolas",12))
        #error_msg2=Label(self, text="Please select password options!", foreground="steelblue", bg="lightsteelblue", font=("Consolas",12))
        try:
            randint_limit=self.get_passwordlength()
        except:
            self.error_msg.configure(text="invalid password length!", foreground="steelblue")
            randint_limit=0
        if self.get_lowervar() ==0 and self.get_uppervar()==0 and self.get_symbolsvar()==0 and self.get_numbersvar()==0:
            self.error_msg.configure(text="Please enter password options!")
            #self.place_errormsg2(to_do=True)
            randint_limit=0

        while randint_limit > 1:
            self.error_msg.configure(text="")
            if self.get_lowervar() == 1:
                limit=random.randint(0,(randint_limit//2))
                if limit==0 and randint_limit>0:
                    limit=1
                for i in range(0, limit):
                    password.append(self.random_lower())
                randint_limit -= limit
            if self.get_uppervar()==1:
                limit=random.randint(0,(randint_limit//2))
                if limit==0 and randint_limit>0:
                    limit=1
                for i in range(0, limit):
                    password.append(self.random_upper())
                randint_limit -= limit
            if self.get_symbolsvar()==1:
                limit=random.randint(0,(randint_limit//2))
                if limit==0 and randint_limit>0:
                    limit=1
                for i in range(0, limit):
                    password.append(self.random_symbol())
                randint_limit -= limit
            if self.get_numbersvar()==1:
                limit=random.randint(0,(randint_limit//2))
                if limit==0 and randint_limit>0:
                    limit=1
                for i in range(0, limit):
                    password.append(self.random_numbers())
                randint_limit -= limit
        while randint_limit==1:
            if self.get_lowervar() == 1:
                limit=random.randint(0,1)
                for i in range(0, limit):
                    password.append(self.random_lower())
                if limit==1:
                    break
            if self.get_uppervar()==1:
                limit=random.randint(0,1)
                for i in range(0, limit):
                    password.append(self.random_upper())
                if limit==1:
                    break
            if self.get_symbolsvar()==1:
                limit=random.randint(0,1)
                for i in range(0, limit):
                    password.append(self.random_symbol())
                if limit==1:
                    break
            if self.get_numbersvar()==1:
                limit=random.randint(0,1)
                for i in range(0, limit):
                    password.append(self.random_numbers())
                if limit==1:
                    break
        random.shuffle(password)
        self.set_password(''.join(password))
        self.display_password()
        self.displayinfo()
        self.clipboard_button()
        self.save_button()
        self.erase_button()

    def display_password(self):
        password_label=Label(self, text=f"Your random password is: ", bg="lightsteelblue", font=("Consolas",14))
        password_label.place(x=720, y=400)
        self.password_change=Text(self, bg="lightsteelblue", font=("Consolas",12), height=1, width=25)
        self.password_change.place(x=980, y=400)
        self.password_change.insert(1.0, f"{self.get_password()}")
        self.password_change.get(1.0, END)
    
    def displayinfo(self):
        info=Label(self, text="You can:\n- Edit the password\n- Save the password to a file\n- Copy the password to your clipboard\n- Erase your password history from the file", bg="lightsteelblue", font=("Consolas",10))
        info.place(x=800, y=480)

    
    def clipboard_button(self):
        save_button = Button(self,text="copy", font=("Consolas", 8),height=1, width=8, bg="lightsteelblue", activebackground="steelblue", activeforeground="pale turquoise", command=self.copytoclipboard)
        save_button.place(x=930, y=600)
    
    def copytoclipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.password_change.get(1.0,END))
        self.update()


    def save_button(self):
        save_button = Button(self,text="Save Password", height=1, width=15, font=("Consolas", 8),bg="lightsteelblue", activebackground="steelblue", activeforeground="pale turquoise", command=self.savetofile)
        save_button.place(x=600, y=600)

    def savetofile(self):
        from datetime import datetime

        with open("saved_passwords.txt", "a") as file:
            if self.password_change.get(1.0,END) in ["poolhouse\n", "pool house\n", "Poolhouse\n", "POOLHOUSE\n", "Pool House\n", "POOL HOUSE\n"]:
                file.write(datetime.now().strftime("%Y-%m-%d_%H.%M.%S")+"  "+ "this song is called dugout..... POOLHOUSE! This- this song is called poolhouse"+ "\n")
                file.write("Waiting around for something to change my mood\n")
                file.write("'Cause I know that what's in these plastic cups isn't going to"+"\n")
                file.write("Kids on the lawn stuck in pairs of two"+"\n")
                file.write("Your lunch is on its way back up"+"\n")
                file.write("But you're still in the pool"+"\n")
                file.write("Wait inside"+"\n")
                file.write("I'll be fine"+"\n")
                file.write("I guess I'll sit outside"+"\n")
                file.write("While you change your mind\n")
                file.write("I'll risk it all to find a place where I can hear my thoughts"+"\n")
                file.write("Songs playing too loud"+"\n")
                file.write("But upstairs they're still making out"+"\n")
                file.write("I'm getting all choked up"+"\n")
                file.write("I guess it's just my luck"+"\n")
                file.write("And I'm stuck on the porch"+"\n")
                file.write("What am I waiting for?"+"\n")
                file.write("Wait inside"+"\n")
                file.write("I'll be fine"+"\n")
                file.write("I guess I'll sit outside"+"\n")
                file.write("While you change your mind"+"\n")
                file.write("Wait inside"+"\n")
                file.write("I'll be fine"+"\n")
                file.write("Wait inside"+"\n")
                file.write("Change your mind"+"\n")
                file.write("Oh, honey, change your mind"+"\n")
                secret_label=Label(self, text=f"check your file :)", bg="lightsteelblue", font=("Consolas",12))
                secret_label.place(x=800, y=900)
            elif str(self.password_change.get(1.0,END))!="poolhouse":
                file.write(datetime.now().strftime("%Y-%m-%d_%H.%M.%S")+"  "+self.password_change.get(1.0, END) + "\n")
    
    def erase_button(self):
        erase_button = Button(self,text="Erase Password", height=1, width=16, font=("Consolas", 8),bg="lightsteelblue", activebackground="steelblue", activeforeground="pale turquoise", command=self.erasefile)
        erase_button.place(x=1200, y=600)

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
root.mainloop()
