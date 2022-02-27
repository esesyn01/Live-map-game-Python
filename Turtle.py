from Animal import Animal
import random
class Turtle(Animal):
    def __init__(self, x, y, world):
        return super().__init__(x, y, 2, 1, -1, "Zolw", world, "zolw.jpg")
    def action(self):
        pass
    def reproduction(self):
        tab=self.check_neighbourhood()
        if tab[0]==-1 or tab[1]==-1 or tab[2]==-1 or tab[3]==-1:
            X=self.get_x()
            Y=self.get_y()
            res=self.randomize_rep(X,Y,tab)
            newborn=Turtle(res[0],res[1],self._world)
            self._world.add(newborn)
            self._world.add_comment("Zolw rozmnaza sie")
    def action(self):
        i=random.randint(0,3)
        if i==1:
            super().action()
        else:
            self.set_countered(1)