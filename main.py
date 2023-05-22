class Bird:

    def __init__(self,name,size):
        self.name=name
        self.size=size


    def fly(self):
        print(f"Un {self.name} est en train de voler")


if __name__=="__main__":    
    b1= Bird("Hirondelle",16)
    b1.fly()