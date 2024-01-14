import customtkinter
from filemngr import *
from PIL import Image
import os
from user import user,Password

#root.withdraw hides root window
#TODO:
#We are going to serialize user object file, then we will convert the key to a bytes string and add them together. Then we will encrypt this string.
#When we decrypt using the key we will test the key with the first n digits of the unencrypted string and if they match we know we have the same user.
#root.update()
#root.deiconify() brings it back into view
user_archive = get_user_archive()
img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','assets/logimg.png'))

#sets the dimensions of the window, and the x/y coordinates to center window
def set_window_dimensions(root):
    width = 450
    height = 400

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    x = (screen_w/2) - (width/2)
    y = (screen_h/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width,height,x,y))

def close_window(root):
        root.destroy()

def update_archive(user_key,user,index):
    archive = get_user_archive()
    key = Fernet(user_key)
    user_bytes = pickle.dumps(user)
    user_encrypted = key.encrypt(user_bytes)
    archive[index] = user_encrypted
    write_to_file(archive)

class LogScreen():
    def __init__(self,root):
        self.toplevel_window = None

        frame = customtkinter.CTkFrame(root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        frame.columnconfigure(0,weight=1)
        frame.columnconfigure(1,weight=1)
        frame.columnconfigure(2,weight=1)
        frame.rowconfigure(0,weight=1)
        frame.rowconfigure(1,weight=1)
        frame.rowconfigure(2,weight=1)
        frame.rowconfigure(3,weight=1)


        label = customtkinter.CTkLabel(frame, text="Welcome,", font=("Roboto",24))
        label.grid(column=1,row=0,padx=10)

        welcome_text = customtkinter.CTkLabel(frame, text="Please enter your key, \nor press generate to create a new key")
        welcome_text.grid(column=1,row=1,padx=10)

        self.pass_entry = customtkinter.CTkEntry(frame, placeholder_text="Enter key")
        self.pass_entry.grid(column=1,row=2,padx=10)

        login_img = customtkinter.CTkImage(light_image=Image.open(img_path),dark_image=Image.open(img_path),size=(30,30))
        login_btn = customtkinter.CTkButton(frame,text="",image=login_img,height=20,width=20,command=lambda a=root: self.log_in(a))
        login_btn.grid(column=2,row=2,sticky='w')

        generate_btn = customtkinter.CTkButton(frame,text="Generate Key",command=lambda: self.generate_key(root))
        generate_btn.grid(column=1,row=3)
    
    def log_in(self,root):
        if self.toplevel_window is None:
            user_archive = get_user_archive()
            key = Fernet(bytes(self.pass_entry.get(),'utf-8'))
            for i,encrypted_user in enumerate(user_archive):
                try:
                    user = key.decrypt(encrypted_user)
                    user = pickle.loads(user)
                    if user.key == bytes(self.pass_entry.get(),'utf-8'):
                        self.toplevel_window = MainScreen(root,user,i)
                        root.withdraw()
                except InvalidToken:
                    pass

    def generate_key(self,root):
        key_window = customtkinter.CTkToplevel(root)
        key_window.geometry("400x175")
        key_window.title("Key Generated")

        warning_msg = customtkinter.CTkLabel(key_window,text="WARNING: This is your unique log-in key, \nkeep it safe and do not lose it. \nThere will be no way to recover this key!")
        warning_msg.pack(pady=10)

        user_key = Fernet.generate_key()
        key_box = customtkinter.CTkTextbox(key_window,font=("Roboto",13),text_color="red",height=10,width=350)
        key_box.insert('0.0',user_key)
        key_box.pack(pady=20,padx=5)
        self.pass_entry.insert(0,user_key)

        #Generate a new user and their encryption key
        new_user = user(user_key)
        #user_data format: [key(44 digits)+user class data]
        user_bytes = pickle.dumps(new_user)
        encrypted_data = t_encrypt_data(user_key,user_bytes)
        user_archive.append(encrypted_data)
        write_to_file(user_archive)

        #write_to_file(user_archive)


#Password Screen after logging in
class PasswordOuterFrame(customtkinter.CTkScrollableFrame):
    def __init__(self,master,user,index,**kwargs):
        super().__init__(master,**kwargs)
        #list to hold the password components
        self.password_comp_list = []
        self.user = user
        self.index = index
        self.width = kwargs["width"]
        #var to hold the edit window so when one window is open, no other windows can open
        self.edit_window = None
        #Holds the PasswordFrame class which invoked the edit window so we have access to that class
        self.password_child = None

        for name,item in self.user.applications.items():
            frame = PasswordFrame(self,name,kwargs["width"])
            frame.update_information(item)

        #PasswordFrame(self,kwargs["width"])
        #PasswordFrame(self,kwargs["width"])
        #PasswordFrame(self,kwargs["width"])
        #PasswordFrame(self,kwargs["width"])
        #PasswordFrame(self,kwargs["width"])
        #PasswordFrame(self,kwargs["width"])
        #PasswordFrame(self,kwargs["width"])
        #PasswordFrame(self,kwargs["width"])
        #PasswordFrame(self,kwargs["width"])
        #PasswordFrame(self,kwargs["width"])
    
    #Makes sure only one instance of an edit window is open
    def check_if_window_open(self):
        if self.edit_window is None or not self.edit_window.window.winfo_exists():
             return True
        return False
    
    #handler function for the edit window
    def update_edit_window(self,child):
        self.password_child = child
        self.edit_window = EditWindow(self,self.password_child)

    def add_password(self,app_name):
        print("temp")
        
class EditWindow():
    def __init__(self,root,child):
        self.child = child
        self.root = root
        self.window = customtkinter.CTkToplevel(root)

        self.window.geometry("300x250")
        self.window.columnconfigure(0,weight=1)
        self.window.columnconfigure(1,weight=2)
        self.window.rowconfigure(0,weight=1)
        self.window.rowconfigure(1,weight=1)
        self.window.rowconfigure(2,weight=1)
        self.window.rowconfigure(3,weight=1)
        self.window.rowconfigure(4,weight=1)
        self.window.rowconfigure(5,weight=1)
        self.window.rowconfigure(6,weight=1)
        self.window.rowconfigure(7,weight=1)
        self.window.rowconfigure(8,weight=1)

        #app name labels
        current_app_lbl = customtkinter.CTkLabel(self.window,text=self.child.app_name)
        current_app_lbl.grid(column=1,row=0)
        app_lbl = customtkinter.CTkLabel(self.window,text="Current App Name:",height=10)
        app_lbl.grid(column=0,row=0,padx=5,sticky='w')
        enter_new_lbl2 = customtkinter.CTkLabel(self.window,text="Enter new ->",font=("Roboto",10))
        enter_new_lbl2.grid(column=0,row=1,sticky='w',padx=5,pady=5)
        self.app_txt = customtkinter.CTkEntry(self.window)
        self.app_txt.grid(column=1,row=1)

        #email labels
        current_email_lbl = customtkinter.CTkLabel(self.window,text=self.root.user.applications[self.child.app_name]["email"])
        current_email_lbl.grid(column=1,row=2)
        email_lbl = customtkinter.CTkLabel(self.window,text="Current Email:",height=10)
        email_lbl.grid(column=0,row=2,padx=5,sticky='w',pady=5)
        enter_new_lbl1 = customtkinter.CTkLabel(self.window,text="Enter new ->",font=("Roboto",10))
        enter_new_lbl1.grid(column=0,row=3,sticky='w',padx=5,pady=5)
        self.email_txt = customtkinter.CTkEntry(self.window)
        self.email_txt.grid(column=1,row=3)

        #user name labels
        current_username_lbl = customtkinter.CTkLabel(self.window,text=self.root.user.applications[self.child.app_name]["username"])
        current_username_lbl.grid(column=1,row=4)
        username_lbl = customtkinter.CTkLabel(self.window,text="Current Username:",height=10)
        username_lbl.grid(column=0,row=4,padx=5,sticky='w',pady=5)
        enter_new_lbl3 = customtkinter.CTkLabel(self.window,text="Enter new ->",font=("Roboto",10))
        enter_new_lbl3.grid(column=0,row=5,sticky='w',padx=5,pady=5)
        self.username_txt = customtkinter.CTkEntry(self.window)
        self.username_txt.grid(column=1,row=5)

        #password labels
        current_password_lbl = customtkinter.CTkLabel(self.window,text=self.root.user.applications[self.child.app_name]["password"])
        current_password_lbl.grid(column=1,row=6)
        password_lbl = customtkinter.CTkLabel(self.window,text="Current Password:",height = 10)
        password_lbl.grid(column=0,row=6,sticky='w',pady=5)
        enter_new_lbl4 = customtkinter.CTkLabel(self.window,text="Enter new ->",font=("Roboto",10))
        enter_new_lbl4.grid(column=0,row=7,sticky='w',padx=5,pady=5)
        self.password_txt = customtkinter.CTkEntry(self.window)
        self.password_txt.grid(column=1,row=7)

        update_btn = customtkinter.CTkButton(self.window,command=self.edit,text="Update")
        update_btn.grid(column=0,row=8)
        

    def edit(self):
        was_updated = False
        new_app_name = self.app_txt.get()
        new_email_name = self.email_txt.get()
        new_username = self.username_txt.get()
        new_password = self.password_txt.get()
        print(self.root.user.applications)
        if new_app_name != '' and new_app_name != self.child.app_name:
            self.root.user.applications[new_app_name] = self.root.user.applications[self.child.app_name]
            del self.root.user.applications[self.child.app_name]
            self.child.app_name = new_app_name
            self.child.app_name_lbl.configure(text=new_app_name)
            was_updated = True
        if new_email_name != '':
            self.root.user.applications[self.child.app_name]["email"] = new_email_name
            self.child.email_name_lbl.configure(text=self.child.censor_email(new_email_name))
            was_updated = True
        if new_username != '':
            self.root.user.applications[self.child.app_name]["username"] = new_username
            self.child.user_name_lbl.configure(text=new_username)
            was_updated = True
        if new_password != '':
            self.root.user.applications[self.child.app_name]["password"] = new_password
            self.child.password_lbl.configure(text=new_password)
            was_updated = True
        if was_updated:
            update_archive(self.root.user.key,self.root.user,self.root.index)
        #self.child.email_name = new_email
        #self.child.email_name_lbl.configure(text=self.child.censor_email(new_email))

app = {"app_name": {

}}

class PasswordFrame():
    def __init__(self,root,name,w_width):
        self.w_width = w_width
        self.app_name = name
        self.email_name = "N/A"
        self.user_name= "N/A"
        self.password = "N/A"
        #Replace this with different components

        self.pass_container = customtkinter.CTkFrame(root,width=self.w_width,height=80,fg_color="gray",border_color=("white"),border_width=1)
        self.pass_container.pack(padx=5,pady=5)
        self.pass_container.bind("<Button-1>",lambda event, a=root: self.edit_password(event,a))
        self.pass_container.pack_propagate(0)
        
        self.pass_container.columnconfigure(0,weight=1)
        self.pass_container.columnconfigure(1,weight=1)
        self.pass_container.columnconfigure(2,weight=3)
        self.pass_container.rowconfigure(0,weight=1)
        self.pass_container.rowconfigure(1,weight=1)
        self.pass_container.rowconfigure(2,weight=1)
        self.pass_container.grid_propagate(0)

        self.app_name_lbl = customtkinter.CTkLabel(self.pass_container,text=self.app_name,anchor="w")
        self.app_name_lbl.grid(row=1,column=0,sticky="w",padx=5)
        #self.app_name_lbl.pack(side="left",padx=5)
        email_name_title_lbl = customtkinter.CTkLabel(self.pass_container,text="Email:",height=11)
        email_name_title_lbl.grid(row=0,column=1)
        self.email_name_lbl = customtkinter.CTkLabel(self.pass_container,text=self.censor_email(self.email_name),height=11,font=("Roboto",11))
        self.email_name_lbl.grid(row=0,column=2)
        #self.email_name_lbl.pack(padx=5,pady=5)
        user_name_title_lbl = customtkinter.CTkLabel(self.pass_container,text="Username:",height=11)
        user_name_title_lbl.grid(row=1,column=1)
        self.user_name_lbl = customtkinter.CTkLabel(self.pass_container,text=self.user_name,height=11,font=("Roboto",11))
        self.user_name_lbl.grid(row=1,column=2)
        #self.user_name_lbl.pack(padx=5,pady=5)
        password_title_lbl = customtkinter.CTkLabel(self.pass_container,text="Password:",height=11)
        password_title_lbl.grid(row=2,column=1)
        self.password_lbl = customtkinter.CTkLabel(self.pass_container,text=self.password,height=11)
        self.password_lbl.grid(row=2,column=2)
        #self.password_lbl.pack(padx=5,pady=5)
        #binding every child object in frame to the event
        for w in self.pass_container.winfo_children():
            w.bind("<Button-1>",lambda event, a=root: self.edit_password(event,a))
    
    #Will want to pull up a screen that allows you to modify the information for that password
    def edit_password(self, event, root):
        if root.check_if_window_open():
            root.update_edit_window(self)

    def update_information(self,user):
        #self.app_name_lbl.configure(text=user.app_name)
        self.email_name_lbl.configure(text=user["email"])
        self.user_name_lbl.configure(text=user["username"])
        self.password_lbl.configure(text=user["password"])

    def censor_email(self,email):
        email = list(email)
        censored_email = []
        censored_email.append(email[0])
        if '@' in email:
            for i,letter in enumerate(email[1:]):
                if letter == '@':
                    censored_email[len(censored_email):] = email[i:]
                    return "".join(censored_email)
                censored_email.append('*')
        else:
            return "".join(email)

          
               

          


class MainScreen():
    def __init__(self,root,current_user,index):
        self.current_user = current_user
        self.user_index = index
        #Creates new window for passwords
        self.main_sc_root = customtkinter.CTkToplevel(root)
        self.main_sc_root.title("Password Manager")
        set_window_dimensions(self.main_sc_root)

        #hotbar components
        hotbar = customtkinter.CTkFrame(self.main_sc_root,width=450,height=35,fg_color=("gray"),border_color=("green"),border_width=1)
        hotbar.pack(pady=0,padx=0)
        hotbar.pack_propagate(0)
        add_pass_btn = customtkinter.CTkButton(hotbar,text="+",font=(("Roboto",15)),text_color=("white"),fg_color=("darkblue"),width=25,height=15,command=self.add_password)
        add_pass_btn.pack(pady=5,padx=0)

        self.frame = PasswordOuterFrame(master=self.main_sc_root,user = self.current_user,index=self.user_index,width=400,height=350,border_width=3,border_color=("darkgreen"),scrollbar_fg_color=("green"),corner_radius=10,scrollbar_button_color=("white"))
        self.frame.pack(pady=15,padx=10)

        
        self.main_sc_root.protocol("WM_DELETE_WINDOW",lambda: close_window(root))


    def add_password(self):
        self.select_name_window = customtkinter.CTkToplevel(self.main_sc_root)
        self.select_name_window.geometry("%dx%d+%d+%d" % (self.main_sc_root.winfo_width(),150,self.main_sc_root.winfo_x(),self.main_sc_root.winfo_y()+self.main_sc_root.winfo_height()/4))
        self.select_name_window.attributes("-topmost",True)
        self.select_name_window.title("New Password")

        txt_lbl = customtkinter.CTkLabel(self.select_name_window,text="Enter new application name")
        txt_lbl.pack()
        self.app_name_entry = customtkinter.CTkEntry(self.select_name_window)
        self.app_name_entry.pack()
        create_pass_btn = customtkinter.CTkButton(self.select_name_window,text="Add",command=self.create_pass)
        create_pass_btn.pack()

    def create_pass(self):
        app_name = self.app_name_entry.get()
        #self.current_user.applications.append(Password(app_name))
        self.current_user.applications[app_name] = {"username": "N/A", "email": "N/A", "password": "N/A"}
        update_archive(self.current_user.key,self.current_user,self.user_index)
        new_frame = PasswordFrame(self.frame,app_name,self.frame.width)
        new_frame.app_name_lbl.configure(text=app_name)
        self.select_name_window.destroy()
        