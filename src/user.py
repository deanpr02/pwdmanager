class user():
    def __init__(self,key):
        self.key = key
        self.applications = {}

class Password():
    def __init__(self):
        self.app_name = '<App_name>'
        self.email_name = 'N/A'
        self.user_name = 'N/A'
        self.password = 'N/A'
    def set_app_name(self,app_name):
        self.app_name = app_name
    def set_email_name(self,email_name):
        self.email_name = email_name
    def set_user_name(self,user_name):
        self.user_name = user_name
    def set_passwor(self,password):
        self.password = password
