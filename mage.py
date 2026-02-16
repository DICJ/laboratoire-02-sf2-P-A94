import random
from personnage import Personnage
from armure import Armure

class Mage(Personnage):
    
    def __init__(self, nom, vie, attaque, mana : int):
        
        armure = Armure("armure magique", 7)
        super().__init__(nom, vie, attaque, armure)
        # protégé
        self._mana = 0
        # validation
        self.mana = mana
        self._mana_max = self.mana
            
    @property
    def mana(self) -> int:
        return self._mana
    
    @mana.setter
    def mana(self, nouveau_mana : int) -> None:
        if nouveau_mana < 0:
            self._mana = 0
        elif nouveau_mana > 100:
            self._mana = 100
        else:
            self._mana = nouveau_mana
            
    def attaquer(self) -> int:
        """fonction attaquer

        Returns:
            int: total des degats
        """
        if self.mana == 0:
                    
           calcul_degat = self.attaque
        
        else:
            calcul_degat = self.attaque + 60
            self.diminuer_mana()
   
        return calcul_degat
        
        
    def diminuer_mana(self) -> None:
        """fonction qui diminue la mana apres chaque attaque

        
        """
        
        reduction = random.randint(15, 25)
        
        self.mana -= reduction
        
    def __str__(self) -> str:
        """description du personnage

        Returns:
            str: phrase decriptive
        """
        
        return f" {self.nom}, vie : {self.vie} pv, attaque : {self.attaque} degats, mana : {self.mana} "
    
    def reset(self) -> None:
        """fonction qui reset la vie et la mana
        """
        self.vie = self._vie_max
        
        self.mana = self._mana_max 
        
    
        
        
    
    
        
        