class Ecole:
    
    def __init__(self,nom,grp_classe=[]):
        self.nom=nom
        self.grp_classe=grp_classe
        print(f"l'école {self.nom} à bien été créé !")
    
    def get_nom(self):
        return self.nom

    def get_grpclasse(self):
        return self.grp_classe

