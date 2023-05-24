from classe import Classe
from ecole import Ecole
from rand import Random
class Ville:

    def __init__(self,nom,ecole_grp=[]):
        self.nom=nom
        self.ecole_grp=ecole_grp
        print(f"la ville {self.nom} à été créé !")

    def get_nom(self):
        return self.nom

    def get_ecole_grp(self):
        return self.ecole_grp
    
    def  generate_rand_school(self,ent): #génère aléatoirement
        for i in range(0,ent):
            alea_name=Random.generer_nom_ville()
            print(f"Ajout de l'école {alea_name}")
            self.ecole_grp.append(Ecole(alea_name))
    
    #Giga fonction pour détailler tout le contenu d'une ville:
        
    def more(self):
        print(f"Ville:{self.get_nom()}")
        for i in self.ecole_grp: #pour chaque école dans une ville
            print(f"|-Ecole {i.get_nom()}")
            for j in i.get_grpclasse(): #pour chaque classe dans une école
                j.view_class()
            
    def generate_all(self,nbr_ecole=2,nbr_class=2,nbr_eleve=1): #génère une ville totalement aléatoire


        self.generate_rand_school(nbr_ecole)
        for school in self.ecole_grp:
            school.addNewRandClass(nbr_class)
            for classe in school.get_grpclasse():
                classe.addRandStudent(nbr_eleve)