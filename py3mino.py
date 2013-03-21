#!/usr/bin/python
#Este es un codigo ilustrativo, no necesariamente funcional.
#This is a ilustative code... not funtional neither part of any project
import random, sys, string, threading, socket, os
AntJugador = "-" 
ProxJugador = "-"
Puntuacion = [0,0]
instanciajugador = []
fila = []
fichas=[]
def createfichas(fichas):
    "crea las fichas "
    for g in range(0,7):
        for x in range(g,7):
            fichas.append([g,x])
createfichas(fichas)
def enfila():
    "devuelve los dos extremos de la fila"
    if fila==[]:
        return [False,False]
    return [fila[0][0],fila[-1][1]]

def bono25(equipo):
    "anade 25 puntos a un equipo x"
    global Puntuacion
    if equipo==0:
        Puntuacion[0] += 25
    else:
        Puntuacion[1] += 25 

class jugador:
    """clase para los jugadores"""
    def __init__(self):
        global instanciajugador
        global fichas
        #almacenar la instancia en una lista
        instanciajugador += [self]
        #definir a que equipo pertenece el jugador
        if instanciajugador.index(self)%2.0==0:
            self.equipo = 0
        else:
            self.equipo = 1
        self.fichas=[]
        jugador.servirse(self)
    @staticmethod
    def servirse(self):
        "el jugador se sirve las 7 fichas"
        for f in range(0,7):
            self.fichas += [random.choice(fichas)]
            fichas.__delitem__(fichas.index(self.fichas[-1]))
        print "el jugador",instanciajugador.index(self),"se ha servido las fichas:",self.fichas
    def __playficha(self,ficha):
        "traslada la ficha desde el jugador a la fila"
        global fila
        self.fichas.__delitem__(self.fichas.index(ficha))
        print "el jugador",instanciajugador.index(self),"ha jugado:",ficha
        if ficha==[6,6] and fila==[]:
            fila = [ficha]
            return
        if enfila()[0] in ficha:
            if enfila()[0] == ficha[1]:
                fila = [ficha]+fila[:]
            else:
                ficha.reverse()
                fila = [ficha]+fila[:]
        else:
            if enfila()[1] == ficha[0]:
                fila += [ficha]
            else:
                ficha.reverse()
                fila += [ficha]
    def play(self):
        "efectua la jugada del jugador x"
        global AntJugador
        global ProxJugador
        global instanciajugador
        global fila
        print "el jugador",instanciajugador.index(self),"va a jugar"
        if AntJugador == "-" and AntJugador == "-" and [6,6] in self.fichas:
            print 'el jugador' , instanciajugador.index(self) , "tiene [6,6]"
            self.__playficha([6,6])
            AntJugador = self
            if instanciajugador.index(self) == 3:
                ProxJugador= instanciajugador[0]
            else:
                ProxJugador=instanciajugador[instanciajugador.index(self)+1]
        elif AntJugador == "-" and ProxJugador==instanciajugador.index(self) and fila == []:
            fila=[random.choice(self.fichas)]
            AntJugador = self
            if instanciajugador.index(self) == 3:
                ProxJugador= instanciajugador[0]
            else:
                ProxJugador=instanciajugador[instanciajugador.index(self)+1]
        elif ProxJugador=="-" and AntJugador=="-" and fila ==[]:
            print "el jugador",instanciajugador.index(self),"no tiene [6,6]"
            return
        else:
            tr=[]
            for t in self.fichas:
                tr+=t[0],t[1]
            if enfila()[0] in tr or enfila()[1] in tr:
                if AntJugador == self and ProxJugador == self:
                    print "paso corrido 25"
                    bono25(self.equipo)
                for i in self.fichas:
                    if enfila()[0] in i or enfila()[1] in i:
                        print "el jugador",instanciajugador.index(self), "tiene las fichas:\n",self.fichas
                        print "el juego esta a",enfila()[0],"y a",enfila()[1]
                        print "la fila es:\n",fila
                        self.__playficha(i)
                        AntJugador = self
                        if instanciajugador.index(self) == 3:
                            ProxJugador= instanciajugador[0]
                        else:
                            ProxJugador=instanciajugador[instanciajugador.index(self)+1]
                        if self.fichas == []:
                            print "Domino!", i
                            AntJugador = "-"
                            ProxJugador = self
                            return ["domino!",i]
                        break
            elif AntJugador == self and ProxJugador == self:
                print 'he trancado el juego'
            else:
                print 'paso!'
                if instanciajugador.index(self) == 3:
                    ProxJugador= instanciajugador[0]
                else:
                    ProxJugador=instanciajugador[instanciajugador.index(self)+1]
for a in range(4):
    jugador()
gh=0
while gh<15:
    for a in instanciajugador:
        a.play()
    gh+=1