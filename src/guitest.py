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
            self.toplevel_window = MainScreen(root)
            root.withdraw()


class MainScreen():
    def __init__(self,root,current_user):
        self.current_user = current_user
        #Creates new window for passwords
        main_sc_root = customtkinter.CTkToplevel(root)
        main_sc_root.title("Password Manager")
        set_window_dimensions(main_sc_root)

        test_lbl = customtkinter.CTkLabel(main_sc_root,text="Password Screen!")
        test_lbl.pack(pady=12,padx=10)
        main_sc_root.protocol("WM_DELETE_WINDOW",lambda: close_window(root))
