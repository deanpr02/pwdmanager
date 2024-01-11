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
          PasswordFrame(self,kwargs["width"],1)
          PasswordFrame(self,kwargs["width"],2)
          PasswordFrame(self,kwargs["width"],3)
          PasswordFrame(self,kwargs["width"],4)
          PasswordFrame(self,kwargs["width"],5)
          PasswordFrame(self,kwargs["width"],6)
          PasswordFrame(self,kwargs["width"],7)
          PasswordFrame(self,kwargs["width"],8)
          PasswordFrame(self,kwargs["width"],9)
          PasswordFrame(self,kwargs["width"],10)

        
class PasswordFrame():
    def __init__(self,root,w_width,key):
        self.w_width = w_width
        self.key = key
        test_frame = customtkinter.CTkFrame(root,width=self.w_width,height=50,fg_color="gray")
        test_frame.pack(padx=5,pady=5)
        test_frame.bind("<Button-1>",lambda event, a=self.key: self.bruh(event,a))
    
    #Will want to pull up a screen that allows you to modify the information for that password
    def bruh(self, event, key):
        print(f"Key: {key}") 
          
               

          


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
