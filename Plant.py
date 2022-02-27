from Organism import Organism
class Plant(Organism):
    def __init__(self,x,y,str,init,age,name,world,img):
        return super().__init__(x,y,str,init,age,name,world,img)
    def action(self):
        pass
    def collision(self):
        pass
    def eat(self,anim):
        X=self.get_x()
        Y=self.get_y()
        if self.get_name()=="Trawa" or self.get_name()=="Mlecz":
            self._world.set_cell(X,Y,anim)
        if self.get_name()=="Guarana":
            str=anim.get_str()
            anim.set_str(str+3)
            self._world.set_cell(X,Y,anim)
        if self.get_name()=="Wilcze jagody":
            anim.set_init(-1)
            anim._world.add_comment(anim.get_name()+" zginal")
            anim.set_name("")
            anim._world.clear_cell(X,Y)
        if self.get_name()=="Barszcz sosnowskiego":
            if anim.get_name()!="Cyberowca":
                anim.set_init(-1)
                anim._world.add_comment(anim.get_name()+" zginal")
                anim.set_name("")
                anim._world.clear_cell(X,Y)
            else:
                self._world.set_cell(X,Y,anim)
        self._world.add_comment(self.get_name()+" zostal zjedzony")
        self.set_name("")
        self.set_init(-1)
        self._world.clear_cell(X,Y)   
    def flee(self):
        pass



