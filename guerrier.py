from personnage import Personnage
from armure import Armure
import random

class Guerrier(Personnage):
    
    def __init__(self, nom, vie, attaque, force : int):
        
        armure = Armure("plaque", 12)
        
        super().__init__(nom, vie, attaque, armure)
        
        self._force = 0
        # validation
        self.force = force
        
    @property
    def force(self) -> int:
        return self._force
    
    @force.setter
    def force(self, nouveau_force : int) -> None:
        if nouveau_force < 0:
            self._force = 0
        elif nouveau_force > 50:
            self._force = 50
        else:
            self._force = nouveau_force
    
    def attaquer(self) -> int:
        """fonction attaquer

        Returns:
            int:le total des degats 
        """
        calcul_degats = int(self.attaque + (self.force / 2) + random.randint(-2, 2))
        
        return calcul_degats
    
    def __str__(self) -> str:
        
        return f" {self.nom}, vie : {self.vie} pv, attaque : {self.attaque} degats, force : {self.force} "