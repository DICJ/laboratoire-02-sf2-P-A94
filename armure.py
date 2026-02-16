

class Armure:
    
    def __init__(self, nom, pts_armure : int):
        
        self.nom = nom
        self._pts_armure = pts_armure
        
    @property
    def pts_armure(self) -> int:
        return self._pts_armure
    
    @pts_armure.setter
    def pts_armure(self, nouveau_armure : int) -> None:
        if nouveau_armure < 0:
            self._pts_armure = 0
        elif nouveau_armure > 15:
            self._pts_armure = 15
        else:
            self._pts_armure = nouveau_armure