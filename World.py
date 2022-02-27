import pygame
import time
from pygame.constants import KEYDOWN
from Antelope import Antelope
from Berry import Berry
from Cybersheep import Cybersheep
from Dandelion import Dandelion
from Fox import Fox
from Grass import Grass
from Guarana import Guarana
from Hogweed import Hogweed
from Human import Human
from Sheep import Sheep
from Turtle import Turtle
from Wolf import Wolf
WORLD_HEIGHT=20
WORLD_WIDTH=20
IMG_RES=23
class World():
    def __init__(self, WORLD_HEIGHT, WORLD_WIDTH):
        self.screen=pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Projekt 2 - Wiktor Kawka 184417")
        self.screen.fill((0,0,0))
        font=pygame.font.SysFont('timesnewroman',14)
        text=font.render("Nacisnij klaiwsz 'L' aby wczytac plik zapisu swiata, inaczej zainicjowany zostanie swiat domyslny" ,True,(255,255,255))
        textr=text.get_rect()
        textr.center=(640,320)
        self.screen.blit(text,textr)
        pygame.display.update()
        self.board=[]
        self.tab_by_init=[]
        self.comment=[]
        self.special=0
        self.end=0
        self.cmd=-1
        for x in range(WORLD_HEIGHT*WORLD_WIDTH):
            self.board.append('NULL')
        while True:
            event=pygame.event.get()
            for x in event:   
                if x.type==pygame.KEYDOWN:
                    if x.key==pygame.K_l:
                        self.load()
                    else:
                        self.start_wrld()
                    self.initialize()
                    return

    def turn(self):
        self.comment.clear()
        self.cmd=self.command()
        if(self.end==1):
            return
        self.sort_for_turn()
        for x in self.tab_by_init:
            if x.get_init()!=-1:
                if x.get_age()!=-1:
                    x.action()
                    x.collision()
                x.aging()
        self.sort_for_turn()
        while self.tab_by_init[-1].get_init()==-1:
            if type(self.tab_by_init[-1]).__name__=="Human":
                self.end=1
            self.tab_by_init.pop()
    def drawrld(self):
        self.screen.fill((0,0,0))
        for i in range(WORLD_WIDTH+1):
            pygame.draw.line(self.screen,(255,0,0),(1+i*26,0),(1+i*26,522),3)
        for i in range(WORLD_HEIGHT+1):
            pygame.draw.line(self.screen,(255,0,0),(0,1+i*26),(522,1+i*26),3)
        self.sort_for_draw()
        for x in self.tab_by_init:
            vimg=pygame.image.load(x.img)
            self.screen.blit(vimg,(4+x.x*26,4+x.y*26))
        font=pygame.font.SysFont('timesnewroman',14)
        for i,x in enumerate(self.comment):
            text=font.render(x,True,(255,255,255))
            textr=text.get_rect()
            textr.center=(850,15+i*15)
            self.screen.blit(text,textr)
        pygame.display.update()
    def get_organism(self,i):
        return self.tab_by_init[i]
    def sort_for_turn(self):
        self.tab_by_init.sort(key=lambda a: (a.init, a.age),reverse=True)
    def sort_for_draw(self):
        self.tab_by_init.sort(key=lambda a: (a.y, a.x))
    def start_wrld(self):
        c1=Cybersheep(5,5,self)
        c2=Cybersheep(2,18,self)
        c3=Cybersheep(9,6,self)
        h1=Hogweed(2,5,self)
        h2=Hogweed(17,2,self)
        h3=Hogweed(1,1,self)
        h4=Hogweed(8,4,self)
        hh=Human(10,10,self)
        d1=Dandelion(18,16,self)
        d2=Dandelion(1,14,self)
        g1=Grass(10,14,self)
        g2=Grass(2,17,self)
        gg1=Guarana(3,7,self)
        gg2=Guarana(15,15,self)
        b1=Berry(14,18,self)
        b2=Berry(1,5,self)
        o1=Sheep(12,18,self)
        o2=Sheep(3,6,self)
        o3=Sheep(9,14,self)
        w1=Wolf(3,14,self)
        w2=Wolf(19,4,self)
        w3=Wolf(5,8,self)
        t1=Turtle(19,15,self)
        t2=Turtle(2,6,self)
        t3=Turtle(5,15,self)
        f1=Fox(6,19,self)
        f2=Fox(16,18,self)
        f3=Fox(8,8,self)
        a1=Antelope(2,9,self)
        a2=Antelope(5,13,self)
        a3=Antelope(13,7,self)
        self.add(c1)
        self.add(c2)
        self.add(c3)
        self.add(h1)
        self.add(h2)
        self.add(h3)
        self.add(h4)
        self.add(hh)
        self.add(d1)
        self.add(d2)
        self.add(g1)
        self.add(g2)
        self.add(gg1)
        self.add(gg2)
        self.add(b1)
        self.add(b2)
        self.add(o1)
        self.add(o2)
        self.add(o3)
        self.add(w1)
        self.add(w2)
        self.add(w3)
        self.add(a1)
        self.add(a2)
        self.add(a3)
        self.add(f1)
        self.add(f2)
        self.add(f3)
        self.add(t1)
        self.add(t2)
        self.add(t3)
    def initialize(self):
        self.sort_for_draw
        for x in self.tab_by_init:
            self.board[x.y*WORLD_WIDTH+x.x]=x
            x.aging()
    def add(self,newborn):
        self.tab_by_init.append(newborn)
        X=newborn.x
        Y=newborn.y
        self.board[Y*WORLD_WIDTH+X]=newborn
    def clear_cell(self, x,y):
        self.board[y*WORLD_WIDTH+x]='NULL'
    def set_cell(self,x,y,org):
        self.board[y*WORLD_WIDTH+x]=org
    def add_comment(self,event):
        self.comment.append(event)
    def command(self):
        while True:
            for event in pygame.event.get():
                if event.type==KEYDOWN and event.key==pygame.K_UP:
                    return 2
                if event.type==KEYDOWN and event.key==pygame.K_DOWN:
                    return 3
                if event.type==KEYDOWN and event.key==pygame.K_LEFT:
                    return 0
                if event.type==KEYDOWN and event.key==pygame.K_RIGHT:
                    return 1
                if event.type==KEYDOWN and event.key==pygame.K_q:
                    self.end=1
                    return -2
                if event.type==KEYDOWN and event.key==pygame.K_z:
                    self.save()
                if event.type==KEYDOWN and event.key==pygame.K_s:
                    if self.special==0:
                        self.special=1
    def load(self):
        file=open("save.txt","r")
        loaded=file.readlines()
        for x in loaded:
            entr=x.split()
            X=int(entr[-2])
            Y=int(entr[-1])
            h=entr[0]
            newb=""
            if h=="Owca":
                newb=Sheep(X,Y,self)
            elif h=="Cyberowca":
                newb=Cybersheep(X,Y,self)
            elif h=="Wilk":
                newb=Wolf(X,Y,self)
            elif h=="Zolw":
                newb=Turtle(X,Y,self)
            elif h=="Lis":
                newb=Fox(X,Y,self)
            elif h=="Antylopa":
                newb=Antelope(X,Y,self)
            elif h=="Czlowiek":
                newb=Human(X,Y,self)
            elif h=="Barszcz":
                newb=Hogweed(X,Y,self)
            elif h=="Wilcze":
                newb=Berry(X,Y,self)
            elif h=="Trawa":
                newb=Grass(X,Y,self)
            elif h=="Guarana":
                newb=Guarana(X,Y,self)
            elif h=="Mlecz":
                newb=Dandelion(X,Y,self)
            self.add(newb) 
        file.close()
    def save(self):
        file=open("save.txt","w")
        cnt=len(self.tab_by_init)
        for i in range(cnt):
            org=self.tab_by_init[i]
            sav=org.get_name()+" "+str(org.get_x())+" "+str(org.get_y())+"\n"
            file.write(sav)
        file.close()
        self.add_comment("Zapisano swiat!")
    def __del__(self):
        pass


    


