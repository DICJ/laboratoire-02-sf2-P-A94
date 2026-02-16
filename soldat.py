from personnage  import Personnage
from armure import Armure

class Soldat(Personnage):
    
    def __init__(self, nom, vie, attaque):
        
        armure = Armure("cotte de maille", 15)
        super().__init__(nom, vie, attaque, armure)
        
    
    def subir_degat(self, degats):
        
        self.vie -= int(degats * 0.90)