#!/usr/bin/python
#*************************************
#           Hang Up Game             *
#    version 1.0 By Dionys Rosario   *
# 2012@copyleft all wrongs reversed  *
#*************************************
import random, os
from random import choice

welcome = '-----Hang up game------\n'
fails = 0 
out=''

#reading the file whit words
xfile=open('words.txt')
txt=xfile.read()

#get our word (Ejemplo) and our list [E,_,_,_,_,_o]
word=choice(txt.split())
basex=word[0] + ' _ ' * (len(word)-2) + word[-1]
base=list(basex.split())
        
while fails<5:
    out=''
    print welcome
    for i in range(0,len(base)):
        out += base[i]+' '       # convert list in a printeable string for display out
    print out
    if "_" not in base:
        break
    char=raw_input('enter a char:\n>')
    os.system('clear')
    if char not in word:
        fails=fails+1
        print '--Looser!', char ,'is not here, you waste', fails , 'of 5 oportunities--'
    else:
        print 'Good! you found', char
        for i in word:
            if i==char:
                j=0
                while word.find(i,j) != -1:
                    base[word.find(i,j)]=char     #replace _ by le char found in the correct index
                    j+=1
if fails<5:
    print 'CONGRATULATIONS you WON!!!!!!!******'
else:
    print 'you loose', 'GAME OVER!!!!', 'the word was: ', word

#Anoder Dimenxion script!!!!