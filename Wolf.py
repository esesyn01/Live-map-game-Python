from Animal import Animal
class Wolf(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, 9, 5, -1, "Wilk", world, "wilk.jpg")
    def reproduction(self):
        tab=self.check_neighbourhood()
        if tab[0]==-1 or tab[1]==-1 or tab[2]==-1 or tab[3]==-1:
            X=self.get_x()
            Y=self.get_y()
            res=self.randomize_rep(X,Y,tab)
            newborn=Wolf(res[0],res[1],self._world)
            self._world.add(newborn)
            self._world.add_comment("Wilk rozmnaza sie")
