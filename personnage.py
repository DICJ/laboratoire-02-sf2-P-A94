from armure import Armure
 
class Personnage :
    
    def __init__ (self, nom : str,  vie : int, attaque : int, armure : Armure):
        # attribut publics
        self.nom = nom
        self.armure = armure
        # attributs protégés
        self._vie = 0
        self._attaque = 0
        #validation
        self.vie = vie
        self.attaque = attaque
        self._vie_max = self.vie
    
    @property
    def vie(self) -> int:
        return self._vie
    
    @vie.setter
    def vie(self, nouveau_pv : int) -> None:
        if nouveau_pv < 0:
            self._vie = 0
        elif nouveau_pv > 500:
            self._vie = 500
        else:
            self._vie = nouveau_pv
            
    @property
    def attaque(self) -> int:
        return self._attaque
    
    @attaque.setter
    def attaque(self, nouveau_attaque : int) -> None:
        if nouveau_attaque < 0:
            self._attaque = 0
        elif nouveau_attaque > 50:
            self._attaque = 50
        else:
            self._attaque = nouveau_attaque
            
    
    def subir_degat(self, degats : int) -> None:
        """fonction pour subir lsw degats d'une attaque

        Args:
            degats (int): degats de l'attaque
        """
              
        self.vie -= degats
        
    
    def attaquer(self) -> None:
        """

        Returns:
            _type_: _description_
        """
        
        calcul_degat = self.attaque
        
        return calcul_degat
    
    def reset(self) -> None:
        
        self.vie = self._vie_max
        
    def __eq__(self, nouveau_perso : "Personnage") -> bool:
        
        if self.nom == nouveau_perso.nom and self.vie == nouveau_perso.vie:
            return True
        
        else:
            return False
        
        
        
    



    
           