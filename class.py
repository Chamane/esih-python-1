import os 

class Fichye:
    """
    Kreye yon klas ki ap pran yon paramèt chemen yon fichye. 
    Epi ki ap gen metòd pou w li, ajoute, efase kontni yo. 
    Epi yon metod pou w efase fichye a si w gen pèmisyon
    """

    def __init__(self, chemenfichye):
        self.chemenfichye = chemenfichye
    
    def lekti(self):
        with open(self.chemenfichye, "r") as f:
            return f.read()

    def ajoute(self, elemanKipouAjoute):
        with open(self.chemenfichye, "a") as f:
            f.write(elemanKipouAjoute)

    def ajoute_devan(self, eleman):
        with open(self.chemenfichye, "r+") as f:
            content = f.read()
            f.write(content+eleman)

    def efase(self):
        os.remove(self.chemenfichye)


class Vivan:
    """
    Kreye yon klas Vivan, ki gen pwopriyete moun (pye, men, non, laj).
    Aprè modelize tèt ou ak yon lòt moun, ki erite klas sa... pa bliye chanjè 
    valè pou yo apwopriye ak moun w ap modelize a.
    Aprè kreye yon klas Poul, ki erite klas s. Pa bliye chanje done ki apwopriye yo.
    """
    def __init__(self, pye, men, non, laj):
        self.pye = pye
        self.men = men
        self.non = non
        self.laj = laj

class Mounn(Vivan):
    pye = 2
    men = 2
    def __init__(self, non, laj):
        pye = Mounn.pye
        men = Mounn.men
        super().__init__(self, pye, men, non, laj)

class Poul(Vivan):
    pye = 2
    men = 0
    def __init__(self, non, laj):
        pye = Poul.pye
        men = Poul.men
        super().__init__(self, pye, men, non, laj)


# dimitri = Mounn("Dimitri Pierre", 25)
# tikok = Poul("Tikòk", 3)

if __name__ == "__main__":
    fichye = Fichye('fichye.txt')

    fichye.ajoute("Eleman ajoute")

    print(fichye.lekti())

    fichye.efase()

    print(vars(dimitri))
    print(vars(tikok))