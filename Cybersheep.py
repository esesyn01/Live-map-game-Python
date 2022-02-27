from Animal import Animal
import math
class Cybersheep(Animal):
    def __init__(self,X,Y,world):
        return super().__init__(X,Y,11,4,-1,"Cyberowca",world,"cyberowca.jpg")
    def reproduction(self):
        tab=self.check_neighbourhood()
        if tab[0]==-1 or tab[1]==-1 or tab[2]==-1 or tab[3]==-1:
            X=self.get_x()
            Y=self.get_y()
            res=self.randomize_rep(X,Y,tab)
            newborn=Cybersheep(res[0],res[1],self._world)
            self._world.add(newborn)
            self._world.add_comment("Cyberowca rozmnaza sie")
    def action(self):
        k=self.seekforhogweed()
        if k==-1:
            super().action()
        else:
            X=self.get_x()
            Y=self.get_y()
            self._world.clear_cell(X, Y)
            if k==0:
                self.set_x(X-1)
            if k==1:
                self.set_x(X+1)
            if k==2:
                self.set_y(Y-1)
            if k==3:
                self.set_y(Y+1)
            self.set_countered(self.attack_countered())
            if self.get_countered()==1:
                self.set_x(X)
                self.set_y(Y)
                self._world.set_cell(X,Y,self)
    def seekforhogweed(self):
        tab=[]
        for x in self._world.tab_by_init:
            if x.get_name()=="Barszcz sosnowskiego":
                tab.append(x)
        if not tab:
            return -1
        X=self.get_x()
        Y=self.get_y()
        res=[]
        for x in tab:
            Xh=x.get_x()
            Yh=x.get_y()
            d=math.sqrt((Xh-X)*(Xh-X)+(Yh-Y)*(Yh-Y))
            res.append((x,d))
        minv=99999
        mint=()
        for x in res:
            if x[1]<minv:
                minv=x[1]
                mint=x[0]
        Xh=mint.get_x()
        Yh=mint.get_y()
        if Yh>Y:
            return 3
        if Yh<Y:
            return 2
        if Xh>X:
            return 1
        return 0
        

