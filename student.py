


class Student:
    def __init__(self,first_name,last_name,age,country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
    def greet(self):
        return f"Hello {self.first_name}{self.last_name}"
    def initials(self):
        return f"Your initials is {self.first_name [0]} {self.last_name [0]}"  
    def yearofbirth(self):
        year= 2022 - self.age
        return f"Your year of birth is {year}"    