from Animal import Animal
class Fox(Animal):
    def __init__(self, x, y, world):
        return super().__init__(x, y, 3, 7, -1, "Lis", world, "lis.jpg")
    def action(self):
        tab=self.check_neighbourhood()
        tab=self.can_move(tab)
        if tab[0]==-1 or tab[1]==-1 or tab[2]==-1 or tab[3]==-1:
            X=self.get_x()
            Y=self.get_y()
            self._world.clear_cell(X, Y)
            self.randomize_inempty(X, Y, tab)
            self.set_countered(self.attack_countered())
            if self.get_countered()==1:
                self.set_x(X)
                self.set_y(Y)
                self._world.set_cell(X,Y,self)
    def reproduction(self):
        tab=self.check_neighbourhood()
        if tab[0]==-1 or tab[1]==-1 or tab[2]==-1 or tab[3]==-1:
            X=self.get_x()
            Y=self.get_y()
            res=self.randomize_rep(X,Y,tab)
            newborn=Fox(res[0],res[1],self._world)
            self._world.add(newborn)
            self._world.add_comment("Lis rozmnaza sie")
    def can_move(self,tab):
        for x in range(4):
            if tab[x]==-1:
                tab[x]=-1
            else:
                if (tab[x]!=-2):
                    org=self._world.get_organism(tab[x])
                    if org.get_str()<=self.get_str():
                        tab[x]=-1
                    else:
                        tab[x]=0
                else:
                    tab[x]=-2
        return tab
