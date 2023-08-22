import tkinter as tk
import os
from pathlib import Path
from guiconfig import *

def main():
    #Create the main window and window frame
    file.file_exists("txt/","user",".txt")
    root = tk.Tk()
    root.title("Password Manager")
    root.geometry("240x240")
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=3)

    # Class instance which creates the login screen; this will allow us to grab the user/password input
    # and store it into variables
    login_screen = LoginScreen(root)

#TODO Check log in credentials from the LoginScreen object; if they match a user in the data base
    #We will move to the next screen with the user passed as a parameter to

    # Main loop
    root.mainloop()


    return 0    

# Main function call
main()





