from abc import ABC
from abc import abstractmethod
import random
class Organism(ABC):
    def __init__(self,x,y,str,init,age,name,world,img):
        self._x=x
        self._y=y
        self._strenght=str
        self._init=init
        self._age=age
        self._name=name
        self._world=world
        self._img=img
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def get_str(self):
        return self._strenght
    def get_init(self):
        return self._init
    def get_age(self):
        return self._age
    def get_name(self):
        return self._name
    def get_world(self):
        return self._world
    def get_img(self):
        return self._img
    def set_x(self,x):
        self._x=x
    def set_y(self,y):
        self._y=y
    def set_str(self,str):
        self._strenght=str
    def set_init(self,init):
        self._init=init
    def set_age(self,age):
        self._age=age
    def set_name(self,name):
        self._name=name
    def set_world(self,world):
        self._world=world
    def set_img(self,img):
        self._img=img
    x=property(get_x,set_x)
    y=property(get_y,set_y)
    strenght=property(get_str,set_str)
    init=property(get_init,set_init)
    age=property(get_age,set_age)
    name=property(get_name,set_name)
    world=property(get_world,set_world)
    img=property(get_img,set_img)
    @abstractmethod
    def action(self):
         pass
    @abstractmethod
    def collision(self):
         pass
    @abstractmethod
    def eat(self,plant):
        pass
    @abstractmethod
    def flee(self):
        pass
    def draw(self):
        pass
    def aging(self):
        self.age=self.age+1
    def left_bound(self):
        if self.x==0:
            return 1
        else:
            return 0
    def right_bound(self):
        if self.x==19:
            return 1
        else:
            return 0
    def upper_bound(self):
        if self.y==0:
            return 1
        else:
            return 0
    def lower_bound(self):
        if self.y==19:
            return 1
        else:
            return 0
    def search(self,X,Y):
        for i,a in enumerate (self._world.tab_by_init):
            if a.x==X and a.y==Y :
                return i
        return -1
    def search_org(self,X,Y,org):
        for i,a in enumerate (self._world.tab_by_init):
            if a.x==X and a.y==Y and a.name==org.name:
                return i
        return -1

    def check_neighbourhood(self):
        tab=[]
        q=self.left_bound()
        if q==0:
            i=self.search(self.x-1,self.y)
            tab.append(i)
        else:
            tab.append(-2)
        q=self.right_bound()
        if q==0:
            i=self.search(self.x+1,self.y)
            tab.append(i)
        else:
            tab.append(-2)
        q=self.upper_bound()
        if q==0:
            i=self.search(self.x,self.y-1)
            tab.append(i)
        else:
            tab.append(-2)
        q=self.lower_bound()
        if q==0:
            i=self.search(self.x,self.y+1)
            tab.append(i)
        else:
            tab.append(-2)
        return tab
    def randomize_move(self,X,Y,tab):
        i=random.randint(0,3)
        while tab[i]==-2:
            i=random.randint(0,3)
        if i==0:
            self.set_x(X-1)
        elif i==1:
            self.set_x(X+1)
        elif i==2:
            self.set_y(Y-1)
        elif i==3:
            self.set_y(Y+1)
    def randomize_inempty(self,X,Y,tab):
        i=random.randint(0,3)
        while tab[i]!=-1:
             i=random.randint(0,3)
        if i==0:
            self.set_x(X-1)
        elif i==1:
            self.set_x(X+1)
        elif i==2:
            self.set_y(Y-1)
        elif i==3:
            self.set_y(Y+1)
    def randomize_rep(self,X,Y,tab):
        i=random.randint(0,3)
        while tab[i]!=-1:
             i=random.randint(0,3)
        if i==0:
            return (X-1,Y)
        elif i==1:
            return (X+1,Y)
        elif i==2:
            return (X,Y-1)
        elif i==3:
            return (X,Y+1)
    def battle(self,second):
        X=self.get_x()
        Y=self.get_y()
        if self.get_str()>second.get_str():
            second._world.add_comment(second.get_name()+" zginal")
            second.set_name("")
            second.set_init(-1)
            second._world.board[Y*20+X]=self
            del second
        else:
            if second.get_str()>self.get_str():
                self._world.add_comment(self.get_name()+" zginal")
                self.set_name("")
                self.set_init(-1)
                self._world.board[Y*20+X]=second
                del self
            else:
                tab=self.check_neighbourhood()
                self.randomize_move(X, Y, tab)
    

