from classe import Classe
from rand import Random
class Ecole:
    
    def __init__(self,nom,grp_classe=[]):
        self.nom=nom
        self.grp_classe=grp_classe
        print(f"l'école {self.nom} à bien été créé !")
    
    def addNewClass(self,nom_c,grp=[]):
        self.grp_classe.append(Classe(nom))

    def addNewRandClass(self,a):
        for i in range(0,a):
            alea_name=Random.generer_nom_ville()
            print(f"Ajout de la classe {alea_name}")
            self.grp_classe.append(Classe(alea_name))

    def get_nom(self):
        return self.nom

    def get_grpclasse(self):
        return self.grp_classe

