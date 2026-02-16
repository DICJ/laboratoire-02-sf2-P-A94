from personnage import Personnage
import random
from detailscombat import DetailsCombat

class Arene:
    
    def __init__(self, liste_personnages : list[Personnage]):
        
        self.liste_personnages = liste_personnages
        self.liste_historique = []
    
    def ajouter_personnage(self, personnage) -> None:
        """ ajouter un personnage

        Args:
            personnage (objet): objet du personnage
        """
        
        self.liste_personnages.append(personnage)
        
    
    def afficher_personnage(self) -> None:
        """afficher les personnages de la liste
        """
        
        if len(self.liste_personnages) == 0:
            print("il n'y a aucun peronnage dans la lite")
        
        else:
            i = 0
            for perso in self.liste_personnages:
                print(f"{i} ) {perso}")
                i += 1
    
    def combattre(self, index_1 : int, index_2 : int) -> None:
        """ faire combattre deux personnages

        Args:
            index_1 (int): indice du premier perso
            index_2 (int): indice du second perso
        """
        
        combat = DetailsCombat(self.liste_personnages[index_1], self.liste_personnages[index_2])
        
        while self.liste_personnages[index_1].vie > 0 and self.liste_personnages[index_2].vie > 0:
            
            degat_attaquant = self.liste_personnages[index_1].attaquer()
            
            self.liste_personnages[index_2].subir_degat(degat_attaquant)
            
            print(f"{self.liste_personnages[index_1].nom} inflige {degat_attaquant} degats à {self.liste_personnages[index_2].nom}")
            
            if self.liste_personnages[index_2].vie <= 0:
                break
            
            sauvegarde_1 = index_1
            sauvegarde_2 = index_2
            
            index_1 = sauvegarde_2
            index_2 = sauvegarde_1
            
            combat.incrementer_tour()
            
        if self.liste_personnages[index_1].vie <= 0:
            gagnant = self.liste_personnages[index_2].nom
        else:
            gagnant = self.liste_personnages[index_1].nom
            
        print(f"Le gagnant du combat est {gagnant}")
        combat.definir_vainqueur(gagnant)
        
        self.liste_historique.append(combat)
        
        
    
    def soigner_perso(self, index : int) -> None:
        """remettre les pv d'un perso

        Args:
            index (int): indice du perso
        """
        self.liste_personnages[index].reset()
        
        print("le personnage a été soigné!")
        
    def nettoyer_arene(self) -> None:
        """enlever tous les perso avec plus de pv de l'arene
        """
        
        for perso in self.liste_personnages:
            if perso.vie <= 0:
                self.liste_personnages.remove(perso)
            
        
    def lancer_battle_royal(self):
        """lancer un battle royale pour trouver le survivant
        """
        
        for perso in self.liste_personnages:
            perso.reset()
        
        while len(self.liste_personnages) > 1:
            combattant = random.randint(0, len(self.liste_personnages) - 1)
            
            if combattant == len(self.liste_personnages) - 1:
                autre_combattant = combattant - 1
            
            else: 
                autre_combattant = combattant + 1
                
            self.combattre(combattant, autre_combattant)
            self.nettoyer_arene()
            
            for perso in range(0, len(self.liste_personnages) - 1):
                self.soigner_perso(perso)
        
        print(f"Le gagnant du battle royale est : {self.liste_personnages[0]}")
    
    def __len__(self) -> int:
        """definition de la grandeur de l'arene

        Returns:
            int: longueur de la liste des peros de l'arene
        """
        
        len = 0
        for perso in self.liste_personnages:
            if perso.vie > 0:
                len += 1
        
        return len
    
    def afficher_historique(self) -> None:
        i = 1
        for combat in self.liste_historique:
            print(f"combat {i}) nombre de tours de combat : {combat.nb_tours + 1}, vainqueur du combat : {combat.vainqueur} ")
            i += 1
    

    
    
            
        
        
            
           
            
            
            
            
            
            
                 