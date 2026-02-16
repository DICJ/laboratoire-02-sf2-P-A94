

class DetailsCombat:
    
    def __init__(self, nom_perso1 : str, nom_perso2 : str,):
        
        self.nom_perso1 = nom_perso1
        self.nom_perso2 = nom_perso2
        self.nb_tours = 0
        self.vainqueur = ""
        
    def incrementer_tour(self) -> None:
        """augmenter le nombre de tours de combat
        """
        self.nb_tours += 1
    
    def definir_vainqueur(self, nom_vainquer : str) -> None:
        """définir le vainqueur du combat

        Args:
            nom_vainquer (str): le gagnant du combat
        """
        self.vainqueur = nom_vainquer