class Etudiant:
    
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        print(f"l'élève {self.name} à été créé !")

    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_age(self):
        return self.age