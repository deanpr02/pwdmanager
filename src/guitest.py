import customtkinter
from PIL import Image
import os

#root.withdraw hides root window

#root.update()
#root.deiconify() brings it back into view
user_archive = []
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

        pass_entry = customtkinter.CTkEntry(frame, placeholder_text="Enter key")
        pass_entry.grid(column=1,row=2,padx=10)

        login_img = customtkinter.CTkImage(light_image=Image.open(img_path),dark_image=Image.open(img_path),size=(30,30))
        login_btn = customtkinter.CTkButton(frame,text="",image=login_img,height=20,width=20,command=lambda: self.button_callback(root))
        login_btn.grid(column=2,row=2,sticky='w')

        generate_btn = customtkinter.CTkButton(frame,text="Log in",command=lambda: self.button_callback(root))
        generate_btn.grid(column=1,row=3)
    
    def button_callback(self,root):
        if self.toplevel_window is None:
            self.toplevel_window = MainScreen(root,"place_holder_user")
            root.withdraw()

#Password Screen after logging in
class PasswordOuterFrame(customtkinter.CTkScrollableFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        #list to hold the password components
        self.password_comp_list = []
        #var to hold the edit window so when one window is open, no other windows can open
        self.edit_window = None
        #Holds the PasswordFrame class which invoked the edit window so we have access to that class
        self.password_child = None

        PasswordFrame(self,kwargs["width"])
        PasswordFrame(self,kwargs["width"])
        PasswordFrame(self,kwargs["width"])
        PasswordFrame(self,kwargs["width"])
        PasswordFrame(self,kwargs["width"])
        PasswordFrame(self,kwargs["width"])
        PasswordFrame(self,kwargs["width"])
        PasswordFrame(self,kwargs["width"])
        PasswordFrame(self,kwargs["width"])
        PasswordFrame(self,kwargs["width"])
    
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
        self.window.grid_rowconfigure(0,minsize=20)

        #app name labels
        current_app_lbl = customtkinter.CTkLabel(self.window,text=self.child.app_name)
        current_app_lbl.grid(column=1,row=0)
        app_lbl = customtkinter.CTkLabel(self.window,text="Current App Name:",height=10)
        app_lbl.grid(column=0,row=0,padx=5,sticky="w")
        enter_new_lbl2 = customtkinter.CTkLabel(self.window,text="Enter new ->",font=("Roboto",10))
        enter_new_lbl2.grid(column=0,row=1,sticky="w",padx=5,pady=5)
        self.app_txt = customtkinter.CTkEntry(self.window)
        self.app_txt.grid(column=1,row=1)

        #email labels
        current_email_lbl = customtkinter.CTkLabel(self.window,text=self.child.email_name)
        current_email_lbl.grid(column=1,row=2)
        email_lbl = customtkinter.CTkLabel(self.window,text="Current Email:",height=10)
        email_lbl.grid(column=0,row=2,padx=5,sticky="w",pady=5)
        enter_new_lbl1 = customtkinter.CTkLabel(self.window,text="Enter new ->",font=("Roboto",10))
        enter_new_lbl1.grid(column=0,row=3,sticky="w",padx=5,pady=5)
        self.email_txt = customtkinter.CTkEntry(self.window)
        self.email_txt.grid(column=1,row=3)

        btn = customtkinter.CTkButton(self.window,command=self.edit)
        btn.grid(column=0,row=5)
        

    def edit(self):
        new_app_name  = 'bruh'
        #self.child.email_name = new_email
        #self.child.email_name_lbl.configure(text=self.child.censor_email(new_email))



class PasswordFrame():
    def __init__(self,root,w_width):
        self.w_width = w_width
        self.app_name = "<App_Name>"
        self.email_name = "N/A"
        self.user_name= "N/A"
        self.password = "N/A"
        #Replace this with different components
        self.test = None

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
    def __init__(self,root,current_user):
        self.current_user = current_user
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

        self.frame = PasswordOuterFrame(master=self.main_sc_root,width=400,height=350,border_width=3,border_color=("darkgreen"),scrollbar_fg_color=("green"),corner_radius=10,scrollbar_button_color=("white"))
        self.frame.pack(pady=15,padx=10)

        
        self.main_sc_root.protocol("WM_DELETE_WINDOW",lambda: close_window(root))


    def add_password(self):
        select_name_window = customtkinter.CTkToplevel(self.main_sc_root)
        select_name_window.geometry("%dx%d+%d+%d" % (self.main_sc_root.winfo_width(),150,self.main_sc_root.winfo_x(),self.main_sc_root.winfo_y()+self.main_sc_root.winfo_height()/4))
        select_name_window.attributes("-topmost",True)
        select_name_window.title("New Password")