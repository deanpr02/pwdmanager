import os
import pickle
import hashlib
from user import user
from pathlib import Path
from cryptography.fernet import Fernet,InvalidToken

#This is the path of the file containing our object file with all of our users along with their attributes.
data_folder = Path("txt")
file_to_open = data_folder / "user.txt"

#Create an encryption key and store it into "key.key"
def write_key():
    key_file = data_folder / "key.key"
    key = Fernet.generate_key()
    with open(key_file,'wb') as keyfile:
        keyfile.write(key)

#This will load the key from the file so we use the same key to encrypt our data to prevent data loss.
def load_key():
    key_file = data_folder / "key.key"
    return open(key_file, "rb").read()

#Checks to see if the file exists; if it does not it will create a file 
#TODO: Modify this function to be more generic so I can create a key file if it does not exist
def if_file_exists(file):
    if not (os.path.exists("txt/user.txt")):
        f = open(file,'a')
        f.close()

def file_exists(dir, file_name, extension):
    file = dir + file_name + extension
    if not (os.path.exists(file)):
        f = open(file,'a')
        f.close()
        return 0
    return 1
if (file_exists("txt/","key",".key") == False):
    write_key()
key = load_key()

def read_file():
    with open(file_to_open,'rb') as file:
        data = pickle.load(file)
        return data
#Writes a user object to the file; this object will be a list of all of the users at our disposal.
def write_to_file(users):
    #decrypt_data()
    with open(file_to_open,'wb') as file:
        pickle.dump(users,file)
    #encrypt_data()

def t_encrypt_data(key,data):
    f = Fernet(key)
    return f.encrypt(data)

def t_decrypt_data(key,data):
    f = Fernet(key)
    return f.decrypt(data)

#Encrypts the data using the key stored in key.key. This gives security so someone cannot just open the file and be able to read all of our users passwords.
def encrypt_data():
    f = Fernet(key)
    with open(file_to_open,'rb') as file:
        data = file.read()
    encrypted_users = f.encrypt(data)
    with open(file_to_open,'wb') as file:
        file.write(encrypted_users)

#Decrypts the data so into usable data that can allow us to read the file when needed.
def decrypt_data():
    if(os.stat(file_to_open).st_size == 0):
        return
    f = Fernet(key)
    with open(file_to_open,'rb') as file:
        try:
            data = file.read()
        except EOFError:
            pass
    decrypted_users = f.decrypt(data)
    with open(file_to_open,'wb') as file:
        file.write(decrypted_users)

#Returns the user from the file which matches the username provided.
def get_user(username):
    fetch_user = ""
    decrypt_data()
    with open(file_to_open,'rb') as file:
        try:
            data = pickle.load(file)
        except EOFError:
            pass
        for item in data:
            if(item.username == username):
                fetch_user = item
                break
    #If fetch_user is not "" then we will want to go to the next screen
    encrypt_data()
    return fetch_user

#Checks to see if a user exists; this will be used to determine if they even exist to prevent errors.
def user_exists(username):
    decrypt_data()
    with open(file_to_open,'rb') as file:
        try:
            data = pickle.load(file)
            for item in data:
                if(item.username == username):
                    encrypt_data()
                    return True
        except EOFError:
            encrypt_data()
            return False
    encrypt_data()
    return False

#Gets the entire user list.
def get_user_archive():
    #decrypt_data()
    with open(file_to_open,'rb') as file:
        try:
            data = pickle.load(file)
        except EOFError:
            return []
    #encrypt_data()
    return data

#updates the application attribute of a user object. This function will add our application passwords per user, for example, user1 can add Facebook: password123 to their object.
def update_user_archive(current_user,key,member):
    decrypt_data()
    with open(file_to_open,'rb') as file:
        try:
            data = pickle.load(file)
        except EOFError:
            pass
        for item in data:
            if(item.username == current_user.username):
                item.applications[key] = member
                break
    encrypt_data()
    write_to_file(data)

#This method will take in a password and return the hashed version of it using the sha256 hashing method
def hash_password(password):
    hash_pass = hashlib.sha256(password.encode())
    return hash_pass.hexdigest()

