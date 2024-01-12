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

class PasswordOuterFrame(customtkinter.CTkScrollableFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        #list to hold the password components
        self.password_comp_list = []
        self.edit_window = None
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
    
    def check_if_window_open(self):
        if self.edit_window is None or not self.edit_window.winfo_exists():
             return True
        return False
    
    def update_edit_window(self,child):
        self.edit_window = customtkinter.CTkToplevel(self)
        self.password_child = child

        btn = customtkinter.CTkButton(self.edit_window,text="press",command=self.edit)
        btn.pack()

    def edit(self):
        self.password_child.test = customtkinter.CTkLabel(self.password_child.pass_container,text="Success")
        self.password_child.test.pack()
        
class PasswordFrame():
    def __init__(self,root,w_width):
        self.w_width = w_width
        self.pass_name = "<Place_holder>"
        #Replace this with different components
        self.test = None

        self.pass_container = customtkinter.CTkFrame(root,width=self.w_width,height=50,fg_color="gray")
        self.pass_container.pack(padx=5,pady=5)
        self.pass_container.bind("<Button-1>",lambda event, a=root: self.edit_password(event,a))
        self.pass_container.pack_propagate(0)

        self.pass_name_lbl = customtkinter.CTkLabel(self.pass_container,text=self.pass_name,anchor="w")
        self.pass_name_lbl.pack(side="left",padx=5)
    
    #Will want to pull up a screen that allows you to modify the information for that password
    def edit_password(self, event, root):
        if root.check_if_window_open():
            root.update_edit_window(self)

          
               

          


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

        frame = PasswordOuterFrame(master=main_sc_root,width=350,height=300,border_width=3,border_color=("darkgreen"),scrollbar_fg_color=("green"),corner_radius=10,scrollbar_button_color=("white"))
        frame.pack(pady=15,padx=10)

        
        main_sc_root.protocol("WM_DELETE_WINDOW",lambda: close_window(root))
