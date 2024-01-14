import tkinter as tk
import os
from pathlib import Path
from guiconfig import *
from guitest import *

def main():
    #Create the main window and window frame
    file.file_exists("txt/","user",".txt")
    root = customtkinter.CTk()
    width = 450
    height = 400

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    x = (screen_w/2) - (width/2)
    y = (screen_h/2) - (height/2)

    root.title("Password Manager")
    root.geometry("%dx%d+%d+%d" % (width,height,x,y))

    # Class instance which creates the login screen; this will allow us to grab the user/password input
    # and store it into variables
    log_in = LogScreen(root)

    # Main loop
    root.mainloop()


    return 0    

# Main function call
if __name__ == "__main__":
    main()

#KEY: viJAyYc3bci3o9T8PtGBVFnt-N68SjWfmD6C924-yRI=



