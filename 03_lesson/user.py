class User:
    def __init__(self, first_name, last_name):
        self.userfirst_name = first_name
        self.userlast_name = last_name
    
    def get_first_name(self):
        print("Моё имя", self.userfirst_name) 
    
    def get_last_name(self):
        print("Моя фамилия", self.userlast_name)
    
    def get_user_info(self):
        print("Моё имя и фамилия:", self.userfirst_name, self.userlast_name)


Alena = User("Alena", "Slinko")
Slinko = User("Slinko", "Alena")


Alena, Slinko.get_user_info()
