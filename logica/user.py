from conection import CConexion


class User:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        

    def __str__(self):
        return f'{self.name} <{self.email}> {self.surname} <{self.surname}> {self.password} <{self.password}>'
    
    def insert_user(self):
        pass
    
    