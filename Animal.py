from Organism import Organism
from abc import abstractmethod
import random
class Animal(Organism):
    def __init__(self,x,y,str,init,age,name,world,img):
        self._countered=0
        super().__init__(x,y,str,init,age,name,world,img)
    def get_countered(self):
        return self._countered
    def set_countered(self,c):
        self._countered=c
    countered=property(get_countered,set_countered)
    def action(self):
        if self.get_init()==-1:
            return
        if self.get_age()==-1:
            return
        tab=self.check_neighbourhood()
        X=self.get_x()
        Y=self.get_y()
        self._world.clear_cell(X,Y)
        self.randomize_move(X,Y,tab)
        self.set_countered(self.attack_countered())
        if self.get_countered()==1:
            self.set_x(X)
            self.set_y(Y)
            self._world.set_cell(X,Y,self)
    def collision(self):
        if self.get_init()==-1:
            return
        if self.get_age()==-1:
            return
        if self.get_countered()==1:
            self.set_countered(0)
            return
        X=self.get_x()
        Y=self.get_y()
        op=self._world.board[Y*20+X]
        if op!='NULL':
            if self.get_name()==op.get_name():
                tab=self.check_neighbourhood()
                if tab[0]==-1 or tab[1]==-1 or tab[2]==-1 or tab[3]==-1:
                    self.randomize_inempty(X,Y,tab)
                    self.collision()
                    if op.get_age()!=-1:
                        self.reproduction()
            else:
                if op.get_name()=="Owca" or op.get_name()=="Cyberowca" or op.get_name()=="Wilk" or op.get_name()=="Czlowiek" or op.get_name()=="Zolw" or op.get_name()=="Lis":
                    self._world.add_comment(self.get_name()+" walczy z "+op.get_name())
                    self.battle(op)
                else:
                    if op.get_name()=="Antylopa":
                        f=op.flee()
                        if f==0:
                            self.battle(op)
                        else:
                             self._world.set_cell(X,Y,self)
                             self._world.add_comment("Antylopa zdolala uciec!")
                    else:
                        op.eat(self)
        else:
             self._world.set_cell(X,Y,self)

    @abstractmethod
    def reproduction(self):
        pass
    def attack_countered(self):
        X=self.get_x()
        Y=self.get_y()
        st=self.get_str()
        op=self._world.board[Y*20+X]
        if op!='NULL':
            if op.get_name() == "Zolw":
                if st<5:
                    self._world.add_comment("Zolw odbija atak")
                    return True
        return False
    def flee(self):
        i=random.randint(0,1)
        if i==1:
            tab=self.check_neighbourhood()
            if tab[0]==-1 or tab[1]==-1 or tab[2]==-1 or tab[3]==-1:
                X=self.get_x()
                Y=self.get_y()
                self.randomize_inempty(X,Y,tab)
                self._world.set_cell(self.get_x(),self.get_y(),self)
                return True
        return False
    def eat(self, plant):
        pass


