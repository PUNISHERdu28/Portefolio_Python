from etudiant import Etudiant
from rand import Random
class Classe:
    
    def __init__(self,nom,groupe=[]):
        self.nom=nom
        self.groupe=groupe
        print(f"la classe {nom} a été créé !")

    def addNewStudent(self,nom,prenom,age):
        self.groupe.append(Etudiant(nom,prenom,age))
        print(f"L'étudiant {c.get_name()} {c.get_surname()} a bien été ajouté")

    def addStudent(self,c):
        self.groupe.append(c)
        print(f"L'étudiant {c.get_name()} {c.get_surname()} a bien été ajouté")

    def addRandStudent(self,inti):
        for i in range(0,inti):
            n,p,a = Random.generer_nom_prenom_age()
            print(f"L'étudiant {n} {p} {a} a bien été créé")
            self.groupe.append(Etudiant(n,p,a))

    
    def get_nom(self):
        return self.nom
    
    def set_nom(self,nom):
        return self.nom
    
    def get_student(self):
        return self.groupe
    
    def set_student(self,grp):
        self.groupe=grp
    
    def age_moyen(self):
        moy=0
        for i in self.groupe:
            moy+=i.get_age()
        
        return moy/len(self.groupe)

    def view_class(self):
    
        print(f"|------Classe:{self.nom}--------")
        for i in self.get_student():
            print(f"|-Elève {i.get_name()} {i.get_surname()} {i.get_age()}")
        print("---------------------------")
