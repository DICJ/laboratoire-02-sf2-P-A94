import random
from personnage import Personnage
from armure import Armure

class Archer(Personnage):
    
    def __init__(self, nom, vie, attaque, dexterite : int):
        
        armure = Armure("tunique de cuir", 5)
        super().__init__(nom, vie, attaque, armure)
        # protégé
        self._dexterite = 0
        
        # validation
        self.dexterite = dexterite
        
    
    @property
    def dexterite(self) -> int:
        return self._dexterite
    
    @dexterite.setter
    def dexterite(self, nouveau_dexterite : int) -> None:
        if nouveau_dexterite < 50:
            self._dexterite = 50
        elif nouveau_dexterite > 100:
            self._dexterite = 100
        else:
            self._dexterite = nouveau_dexterite
            
    def attaquer(self) -> int:
        """fonction attaquer

        Returns:
            int: les dégats de l'attaque
        """
        
        nb_aleatoire = random.randint(0, 100)
        
        if self._dexterite > nb_aleatoire:
            calcul_degats = (self.attaque + 15) * 2
        
        else:
            calcul_degats = self.attaque + 15
             
        return calcul_degats
    
    def __str__(self) -> str:
        """description du personnage

        Returns:
            str: pharse de description du perso
        """
        
        return f" {self.nom}, vie : {self.vie} pv, attaque : {self.attaque} degats, dextérité : {self.dexterite} "

