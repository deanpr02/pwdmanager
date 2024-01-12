import customtkinter

#root.withdraw hides root window

#root.update()
#root.deiconify() brings it back into view

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

        label = customtkinter.CTkLabel(frame, text="Welcome", font=("Roboto",24))
        label.pack(pady=12, padx=10)

        user_entry = customtkinter.CTkEntry(frame, placeholder_text="Username")
        user_entry.pack(pady=12, padx=10)

        pass_entry = customtkinter.CTkEntry(frame, placeholder_text="Password")
        pass_entry.pack(pady=12,padx=10)

        login_btn = customtkinter.CTkButton(frame,text="Log in",command=lambda: self.button_callback(root))
        login_btn.pack(pady=12,padx=10)
    
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

        
class EditWindow():
    def __init__(self,root,child):
        self.child = child
        self.window = customtkinter.CTkToplevel(root)

        email_lbl = customtkinter.CTkLabel(self.window,text="Email:")
        email_lbl.pack()
        self.email_txt = customtkinter.CTkEntry(self.window)
        self.email_txt.pack()
        confirm_btn = customtkinter.CTkButton(self.window,text="press",command=self.edit)
        confirm_btn.pack()

    def edit(self):
        new_email = self.email_txt.get()
        self.child.email_name = new_email
        self.child.email_name_lbl.configure(text=self.child.censor_email(new_email))



class PasswordFrame():
    def __init__(self,root,w_width):
        self.w_width = w_width
        self.app_name = "<App_Name>"
        self.email_name = "email@gmail.com"
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
    
    #Will want to pull up a screen that allows you to modify the information for that password
    def edit_password(self, event, root):
        if root.check_if_window_open():
            root.update_edit_window(self)

    def censor_email(self,email):
        email = list(email)
        censored_email = []
        censored_email.append(email[0])
        for i,letter in enumerate(email[1:]):
            if letter == '@':
                censored_email[len(censored_email):] = email[i:]
                return "".join(censored_email)
            censored_email.append('*')



          
               

          


class MainScreen():
    def __init__(self,root,current_user):
        self.current_user = current_user
        #Creates new window for passwords
        main_sc_root = customtkinter.CTkToplevel(root)
        main_sc_root.title("Password Manager")
        set_window_dimensions(main_sc_root)

        #hotbar components
        hotbar = customtkinter.CTkFrame(main_sc_root,width=450,height=35,fg_color=("gray"),border_color=("green"),border_width=1)
        hotbar.pack(pady=0,padx=0)
        hotbar.pack_propagate(0)
        add_pass_btn = customtkinter.CTkButton(hotbar,text="+",font=(("Roboto",15)),text_color=("white"),fg_color=("darkblue"),width=25,height=15)
        add_pass_btn.pack(pady=5,padx=0)

        frame = PasswordOuterFrame(master=main_sc_root,width=400,height=350,border_width=3,border_color=("darkgreen"),scrollbar_fg_color=("green"),corner_radius=10,scrollbar_button_color=("white"))
        frame.pack(pady=15,padx=10)

        
        main_sc_root.protocol("WM_DELETE_WINDOW",lambda: close_window(root))
