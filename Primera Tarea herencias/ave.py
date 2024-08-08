from datetime import datetime
from  animal import animal
class ave(animal):
    def __init__(self,nacimiento,propietario,nombre1,peso1):
        self.fecha=nacimiento
        self.dueño=propietario
        super().__init__(nombre1,peso1)
        
    def condicion(self):
        now = datetime.now()
        fec=(now.year)
        nacimiento=fec-self.fecha
        print("su edad es:",nacimiento)
        if (nacimiento>5):
            print("es mayor de edad")
        else:
            print("es menor de edad")
            
B=ave(2000,"jose","asd",9)
B.condicion()