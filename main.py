from etudiant import Etudiant
from classe import Classe
from ecole import Ecole
from ville import Ville

def initialisation():
    
    e1 = Etudiant("Jhon","Doe",15)
    
    grp = [
        e1,
        Etudiant("Walid","Taleb",35),
        Etudiant("Therence","Boisgard",23),
        Etudiant("Velan","Segutuvan",24),
        Etudiant("Raphael","Marouani",23)
    ]

    e2=Etudiant("Jean","Claude",35)
    e3=Etudiant("Van","Damn",35)
    e4=Etudiant("Victor","Chuun",35)
    e5=Etudiant("Kevin","Leroux",35)

    print("Création des classes")
    
    c2 = Classe("M2 IRS")
    c1 = Classe("M1 IRS",grp)
    

    print("Incrémentation d'élèves dans la classe")

    c2.addStudent(e2)
    c2.addStudent(e3)
    c2.addStudent(e4)
    c2.addStudent(e5)

    print("Vue sur les classes")
    
    c1.view_class()
    c2.view_class()

    print("Moyenne d'age des classes de cours:")
    print(f"M1-IRS:{c1.age_moyen()}\nM2-IRS:{c1.age_moyen()}\n\n\n\n")   

    print("Déclaration de l'école:")

    ecole1= Ecole("AFORP",[c1,c2])


    print("\nDéclaration de Ville")

    ville1 = Ville("Issy-les-Moulineaux",[ecole1])

    print("\nDéroulé d'une ville généré")
    ville1.more()

if __name__=="__main__":    
    initialisation()