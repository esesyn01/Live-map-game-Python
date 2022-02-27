from Animal import Animal
class Antelope(Animal):
    def __init__(self,X,Y,world):
        return super().__init__(X,Y,4,4,-1,"Antylopa",world,"anty.jpg")
    def reproduction(self):
        tab=self.check_neighbourhood()
        if tab[0]==-1 or tab[1]==-1 or tab[2]==-1 or tab[3]==-1:
            X=self.get_x()
            Y=self.get_y()
            res=self.randomize_rep(X,Y,tab)
            newborn=Antelope(res[0],res[1],self._world)
            self._world.add(newborn)
            self._world.add_comment("Antylopa rozmnaza sie")
    def action(self):
        super().action()
        if self.get_init()==-1:
            return
        self.collision()
        if self.get_init()==-1:
            return
        super().action()
