from classe import Classe

class Ville:

    def __init__(self,nom,ecole_grp=[]):
        self.nom=nom
        self.ecole_grp=ecole_grp
        print(f"la ville {self.nom} à été créé !")

    def get_nom(self):
        return self.nom

    def get_ecole_grp(self):
        return self.ecole_grp
    #Giga fonction pour détailler tout le contenu d'une ville:
    def more(self):
        print(f"Nom de la VIlle:{self.get_nom()}")
        for i in self.ecole_grp: #pour chaque école dans une ville
            print(f"Ecole {i.get_nom()}")
            for j in i.get_grpclasse(): #pour chaque classe dans une école
                j.view_class()
            