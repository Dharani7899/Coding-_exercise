class Teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
            print(f"Name:{self.name} REgno:{self.regno}")
           
t1=Teacher("Dniya",20)
t2=Teacher("mania",89)   
t1.display()
t2.display()         