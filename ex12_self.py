class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__password = password
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
     
    def set_email(self, email):
        self.email = email
    
    def get_email(self):
        return self.email
    
    def set_password(self, password):
        self.__password = password
    
    def get_password(self):
        return self.__password
    
    def find_all(self):
        return f"Your account: User:{self.name} Email:{self.email} Password{self.__password}"