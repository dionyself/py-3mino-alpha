#!/usr/bin/python
import ramdon, sys
fichas = [[0,0][0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[2,2],[2,3],[2,4],[2,5],[2,6],[3,3],[3,4],[3,5],[3,6],[4,4],[4,5],[4,6],[5,5],[5,6],[6,6]]
AntJugador = ""
ProxJugador = 0
Puntuacion = [0,0]
instaciajugador = []
fila = []

def enfila():
    return [fila[0][0],fila[-1][1]]

def bono25(equipo):
    global Puntuacion
    if equipo==0:
        Puntuacion[0] += 25
    else:
        Puntuacion[1] += 25 

class jugador:
    """clase para los jugadores"""
    def __init__(self):
        global instanciajugador
        instaciajugador += [self]
        if self == instanciajugador[0] or self == instanciajugador[2]:
            self.equipo = 0
        else:
            self.equipo = 1
        self.fichas = []
    def __playficha(self,ficha):
        fila += [6,6]
        self.fichas.__delitem__(self.fichas.index([6,6]))
            
    def play(self):
        global AntJugador
        global ProxJugador
        if AntJugador == "" and [6,6] in self.fichas:
            print 'el jugador' + instanciajugador.index(self) + "tiene [6,6]"
            self.__playficha([6,6])
            AntJugador = self
            if instanciajugador.index(self) == 3:
                ProxJugador= instanciajugador[0]
            else:
                ProxJugador=instanciajugador[instanciajugador.index(self)+1]
        elif fila == "":
            self.__playficha(ramdon.choise(self.fichas))
        else:
            if enfila()[0] in self.fichas or enfila()[1] in self.fichas:
                if AntJugador == self and ProxJugador == self:
                    print "paso corrido 25"
                    bono25(self.equipo)
                for i in self.fichas:
                    if enfila()[0] or enfila()[1] in i:
                        self.__playficha(i)
                        AntJugador = self
                        if instanciajugador.index(self) == 3:
                            ProxJugador= instanciajugador[0]
                        else:
                            ProxJugador=instanciajugador[instanciajugador.index(self)+1]
                        if self.fichas == "":
                            print "Domino!", i
                            AntJugador = ""
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
for a in range(3):
	jugador()
while True:
	for a in instanciajugadores:
		a.play()
	