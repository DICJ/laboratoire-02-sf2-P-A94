from guerrier import Guerrier
from archer import Archer
from mage import Mage
from arene import Arene

liste_personnages = []
arene = Arene(liste_personnages)

choix = 1000
while choix != 0:
    print("--------------------------Menu---------------------------")
    print("1) créer un personnage")
    print("2) afficher les personnages de l'arène")
    print("3) combat dans l'arène")
    print("4) soigner un personnage")
    print("5) nettoyer l'arène")
    print("6) nombre de combattant dans l'arène")
    print("7) lancer le battle royale")
    print("8) voir historique des combats")
    print("9) quitter")
    
    option = int(input("Quel option voulez-vous faire (numero) : "))
    
    match option:
        case 1:# créer perso
            nom = input("quel est le nom de votre personnage : ")
            attaque = int(input("combien d'attaque à votre perso : "))
            vie = int(input("combien de vie a votre perso : "))
            type = input("quel est le type de votre personnage (Guerrier, Mage, Archer) : ")
            
            match type:
                case "Guerrier":
                    force = int(input("quel est la force de votre guerrier ? : "))
                    
                    nom = Guerrier(nom, vie, attaque, force)
                    arene.ajouter_personnage(nom)
                
                case "Mage":
                    mana = int(input("combien de mana a votre mage : "))
                    
                    nom = Mage(nom, vie, attaque, mana)
                    arene.ajouter_personnage(nom)
                
                case "Archer":
                    dexterite = int(input("combien de dextérité a votre archer : "))
                    
                    nom = Archer(nom, vie, attaque, dexterite)
                    arene.ajouter_personnage(nom)
                
                case _:
                    print("entrer un type valide svp")
        
        
        case 2: # afficher les perso dans l'arene
            arene.afficher_personnage()
        
        case 3: # combat dans l'arene
            arene.afficher_personnage()
            
            indice_1 = int(input("quel est l'indice du premier personnage qui fera le combat ? : "))
            indice_2 = int(input("quel est l'indice du deuxieme personnage qui fera le combat ? : "))
            
            arene.combattre(indice_1, indice_2)
        
        case 4: # soigner les pv d'un perso
            arene.afficher_personnage()
            
            indice_1 = int(input("quel et l'indice du personnage que vous voulez soigner? : "))
            
            arene.soigner_perso(indice_1)
        
        case 5: # enlever tous les perso morts de l'arene
            arene.nettoyer_arene()
            
            print("l'arene est nettoyer !")
        
        case 6: # afficher le nb de combattants dans l'arene
            print(f" Il y a {len(arene)} combattants dans l'arène")
        
        case 7: # lancer un battle royale
            arene.lancer_battle_royal()
        
        case 8: # voir historique des combats
            arene.afficher_historique()
            
        case 9: # quitter
            choix = 0
        
        case _:
            print("veuillez choisir une option valide svp")

print("fin du prgramme")
            
            
                
                
         
            
            
            
    
    
    