import tkinter as tk
import filemngr as file
from functools import partial
from user import user
#TODO check if the file containing username/password info exists and if it does then open it and check to see
#If the password matches the username;

#This list will store all of the users we create
user_archive = []

#The initial log in screen which handles if a user exists and the creation of a user along with the logging in functionality.
class LoginScreen():
    def __init__(self, root):
        # Instance Variables
        self.user_input = ""
        self.pass_input = ""

        # Welcome label
        self.welcome_label = tk.Label(root,text="Welcome",font=("Arial",15))
        self.welcome_label.place(relx=0.5,rely=0.1,anchor="center")
        # Username label
        self.username_label = tk.Label(root,text="Username")
        self.username_label.grid(pady=(50,10),column=0,row=1)
        # Password label
        self.password_label = tk.Label(root,text="Password")
        self.password_label.grid(column=0,row=2)
        # Entry box for username
        self.username_box = tk.Entry(root)
        self.username_box.grid(column=1,row=1,pady=(50,10),padx=(0,10))
        # Entry box for password; it will appear censored
        self.password_box = tk.Entry(root,show="*")
        self.password_box.grid(column=1,row=2,padx=(0,10))
        # Log in button; when pressed it will run the get_credentials function
        self.login_btn = tk.Button(root,text="Log in",command=partial(self.check_credentials,root))
        self.login_btn.grid(column=1,row=3,sticky=tk.E,padx=25,pady=10)
        #Error Label
        self.error_label = tk.Label(root,text="",fg="red")
        self.error_label.grid(row=4,column=1,sticky='W')
        #Create user button
        self.create_btn = tk.Button(root,text="Create User",command=self.create_user)
        self.create_btn.grid(column=0,row=3,sticky='W',padx=20,pady=10)

    #Checks to see if the username exists and if the password matches; note the passwords are hashed. If they do match the user will be able to proceed to the next screen.
    def check_credentials(self,root):
        self.user_input = self.username_box.get()
        self.pass_input = self.password_box.get()
        if(file.user_exists(self.user_input)):
            current_user = file.get_user(self.user_input)
            if(str(file.hash_password(self.pass_input)) == current_user.password):
                #Then we give access to user
                root.destroy()
                new_root = tk.Tk()
                new_root.title("The Vault")
                new_root.geometry("240x75")
                new_root.columnconfigure(0,weight=1)
                new_root.columnconfigure(1,weight=2)
                new_root.columnconfigure(2,weight=3)
                user_screen = UserScreen(new_root,current_user)

            else:
                self.error_label.config(text="Wrong password")
        else:
            self.error_label.config(text="User does not exist")

    #Creates a new user; if a username already exists it will display an error message.
    def create_user(self):
        new_username = self.username_box.get()
        new_password = self.password_box.get()
        user_list = file.get_user_archive()
        if(file.user_exists(new_username)):
            self.error_label.config(text="Username already exists")
            return
        if(len(new_password) <= 3):
            self.error_label.config(text="Pass too short")
            return
        hashed_password = str(file.hash_password(new_password))
        user_list.append(user(new_username,hashed_password))
        file.write_to_file(user_list)
        self.error_label.config(text="User created")
        self.username_box.delete(0,'end')
        self.password_box.delete(0,'end')


#The user screen where you can look up your own personal passwords you have added.
class UserScreen():
    def __init__(self,root,current_user):
        #The current user is a user class object with username, password, and applications attributes
        self.current_user = current_user
        
        #Request label
        self.request_label = tk.Label(root,text="Request App")
        self.request_label.grid(column=0,row=1)

        #Entry box
        self.entry_box = tk.Entry(root)
        self.entry_box.grid(column=1,row=1)

        #Receive button
        self.retrieve_button = tk.Button(root,text="Retrieve",command=self.retrieve_data)
        self.retrieve_button.grid(column=0,row=2)

        #Add button
        self.add_button = tk.Button(root,text="Add",command=partial(self.add_data,root))
        self.add_button.grid(column=3,row=2,padx=(0,15))

        #Retrieve data function
    def retrieve_data(self):
        requested = file.get_user(self.current_user.username).applications[self.entry_box.get()]
        r = tk.Tk()
        r.geometry("200x50")
        r.title(self.entry_box.get())
        req_label = tk.Label(r,text=requested)
        req_label.place(relx=0.5,rely=0.5,anchor="center")
        #I'll want to store the keys aka application names such as facebook in all lowercase, so
        #Once the input is read we will .lowercase() to make sure we dont have any capital letters

        #Add password
    def add_data(self,root):
        temp_root = tk.Tk()
        temp_root.title = "Add Password"
        temp_root.geometry("200x150")
        temp_root.columnconfigure(0,weight=1)
        temp_root.columnconfigure(1,weight=3)
        temp = TempWindow(temp_root,self.current_user)

#Temp window is a window that is created when adding a new password and then it is destroyed after that.
class TempWindow():
    def __init__(self,root,user):
        self.user_input =""
        self.pass_input=""
        self.current_user = user
    #Enter app name and password labels
        self.enter_label = tk.Label(root,text="Enter App Name")
        self.enter_label.grid(column=0,row=0)
        self.pass_label = tk.Label(root,text="Enter password")
        self.pass_label.grid(column=0,row=1)
        #The entry boxes to receive the data
        self.user_entry = tk.Entry(root)
        self.user_entry.grid(column=1,row=0)
        self.pass_entry = tk.Entry(root)
        self.pass_entry.grid(column=1,row=1)
        #Button to trigger the event
        self.trigger_btn = tk.Button(root,text="Log",command=partial(self.log_data,root))
        self.trigger_btn.grid(column=0,row=2)

    #Log the new user name and password
    def log_data(self,root):
        file.update_user_archive(self.current_user,self.user_entry.get(),self.pass_entry.get())
        root.destroy()