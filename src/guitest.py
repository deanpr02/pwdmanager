import customtkinter
from functools import partial

def test():
    print("test")

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
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            screen = MainScreen(root)
        else:
            self.toplevel_window.focus()


class MainScreen():
    def __init__(self,root):
        #Creates new window for passwords
        self.current_window = None
        new_root = customtkinter.CTkToplevel(root)
        width = 450
        height = 400

        screen_w = new_root.winfo_screenwidth()
        screen_h = new_root.winfo_screenheight()

        x = (screen_w/2) - (width/2)
        y = (screen_h/2) - (height/2)

        new_root.title("Password Manager")
        #root.geometry("450x400")
        new_root.geometry("%dx%d+%d+%d" % (width,height,x,y))
        test_lbl = customtkinter.CTkLabel(new_root,text="Password Screen!")
        test_lbl.pack(pady=12,padx=10)
        new_root.protocol("WM_DELETE_WINDOW",lambda: self.close_window(root))

    def close_window(self,root):
        root.destroy()
