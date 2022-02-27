from Plant import Plant
import random
class Guarana(Plant):
    def __init__(self, x, y, world):
        return super().__init__(x, y, 0, 0, -1, "Guarana", world, "guarana.png")
    def action(self):
        tab=self.check_neighbourhood()
        if tab[0]==-1 or tab[1]==-1 or tab[2]==-1 or tab[3]==-1:
            X=self.get_x()
            Y=self.get_y()
            i=random.randint(0,9)
            if i==5:
                res=self.randomize_rep(X, Y, tab)
                newborn=Guarana(res[0],res[1],self._world)
                self._world.add(newborn)
                self._world.add_comment("Guarana rozmnaza sie")
