from Animal import Animal
import random
class Human(Animal):
    def __init__(self, x, y, world):
        self._cooldown=0
        return super().__init__(x, y, 5, 4, -1, "Czlowiek", world, "czlowiek.jpg")
    def get_cd(self):
        return self._cooldown
    def set_cd(self,c):
        self._cooldown=c
    cooldown=property(get_cd,set_cd)
    def action(self):
        self.start_spell()
        factor=1
        if self.get_cd()>7:
            factor=2
        else:
            if self.get_cd()>4:
                c=random.randint(0,1)
                factor+=c
        comm=self._world.cmd
        X=self.get_x()
        Y=self.get_y()
        tempx=X
        tempy=Y
        self._world.clear_cell(X,Y)
        tab=self.check_neighbourhood()
        if comm==0:
            if tab[0]!=-2:
                X-=factor
        elif comm==1:
            if tab[1]!=-2:
                X+=factor
        elif comm==2:
            if tab[2]!=-2:
                Y-=factor
        elif comm==3:
            if tab[3]!=-2:
                Y+=factor
        if X<0 or X>19:
            X=tempx
        if Y<0 or Y>19:
            Y=tempy
        self.set_x(X)
        self.set_y(Y)
        if self.get_cd()>0:
            self.set_cd(self.get_cd()-1)
        if self.get_cd()==0:
            self._world.special=0
    def start_spell(self):
        if self._world.special==1:
            if self.get_cd()>0:
                self._world.add_comment("Umiejetnosc odnowi sie za "+str(self.get_cd())+" rund")
            else:
                self.set_cd(10)
                self._world.add_comment("Aktywowano umiejetnosc specjalna")
    def reproduction(self):
        pass
