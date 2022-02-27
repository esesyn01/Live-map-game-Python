from Plant import Plant
import random
class Hogweed(Plant):
    def __init__(self, x, y, world):
        return super().__init__(x, y, 10, 0, -1, "Barszcz sosnowskiego", world, "barszcz.jpg")
    def action(self):
        tab=self.check_neighbourhood()
        for c in range(4):
            if tab[c]!=-1:
                org=self._world.get_organism(tab[c])
                if org.get_name()=="Owca" or org.get_name()=="Wilk" or org.get_name()=="Lis" or org.get_name()=="Zolw" or org.get_name()=="Antylopa" or org.get_name()=="Czlowiek":
                    org.set_init(-1)
                    org._world.add_comment(org.get_name()+" zginal")
                    org.set_name("")
                    org._world.clear_cell(org.get_x(),org.get_y())
                    tab[c]=-1
        if tab[0]==-1 or tab[1]==-1 or tab[2]==-1 or tab[3]==-1:
            X=self.get_x()
            Y=self.get_y()
            i=random.randint(0,9)
            if i==5:
                res=self.randomize_rep(X, Y, tab)
                newborn=Hogweed(res[0],res[1],self._world)
                self._world.add(newborn)
                self._world.add_comment("Barsz sosnowskiego rozmnaza sie")
