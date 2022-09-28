from tkinter import *
import tkinter.font as font
from time import *
from time import *

fenetre = Tk()
# Création de la fenêtre de jeu
fenetre.title("Blackjack solo")
# Nom de la fenêtre
fenetre.config(bg="#1b1b1b")
# Couleur du fond de la fenêtre
fenetre.attributes('-fullscreen', True)
# Taille de la fenêtre

def quitter():
    """Ferme la fenêtre lorsqu'on clique sur le bouton correspondant"""
    fenetre.destroy()

def c1():
    if bouton_c1['text'] == '':
        bouton_c1['fg'] = 'blue'
        bouton_c1['text'] = 'X'
        if bouton_c2['text'] == 'X' and bouton_c3['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c4['text'] == 'X' and bouton_c7['text'] == 'X':
            actu.set("C'est gagné !")
        ia()
        if bouton_c1['text'] == 'O' and bouton_c2['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c4['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c6['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c8['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c4['text'] == 'O' and bouton_c7['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c2['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c8['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c9['text'] == 'O' and bouton_c6['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
    else:
        actj.set("Cette emplacement est déjà pris !")

def c2():
    if bouton_c2['text'] == '':
        bouton_c2['fg'] = 'blue'
        bouton_c2['text'] = 'X'
        if bouton_c1['text'] == 'X' and bouton_c3['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c5['text'] == 'X' and bouton_c8['text'] == 'X':
            actu.set("C'est gagné !")
        ia()
        if bouton_c1['text'] == 'O' and bouton_c2['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c4['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c6['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c8['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c4['text'] == 'O' and bouton_c7['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c2['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c8['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c9['text'] == 'O' and bouton_c6['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
    else:
        actj.set("Cette emplacement est déjà pris !")

def c3():
    if bouton_c3['text'] == '':
        bouton_c3['fg'] = 'blue'
        bouton_c3['text'] = 'X'
        if bouton_c2['text'] == 'X' and bouton_c1['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c6['text'] == 'X' and bouton_c9['text'] == 'X':
            actu.set("C'est gagné !")
        ia()
        if bouton_c1['text'] == 'O' and bouton_c2['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c4['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c6['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c8['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c4['text'] == 'O' and bouton_c7['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c2['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c8['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c9['text'] == 'O' and bouton_c6['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
    else:
        actj.set("Cette emplacement est déjà pris !")

def c4():
    if bouton_c4['text'] == '':
        bouton_c4['fg'] = 'blue'
        bouton_c4['text'] = 'X'
        if bouton_c1['text'] == 'X' and bouton_c7['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c5['text'] == 'X' and bouton_c6['text'] == 'X':
            actu.set("C'est gagné !")
        ia()
        if bouton_c1['text'] == 'O' and bouton_c2['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c4['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c6['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c8['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c4['text'] == 'O' and bouton_c7['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c2['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c8['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c9['text'] == 'O' and bouton_c6['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
    else:
        actj.set("Cette emplacement est déjà pris !")

def c5():
    if bouton_c5['text'] == '':
        bouton_c5['fg'] = 'blue'
        bouton_c5['text'] = 'X'
        if bouton_c4['text'] == 'X' and bouton_c6['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c8['text'] == 'X' and bouton_c2['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c9['text'] == 'X' and bouton_c1['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c3['text'] == 'X' and bouton_c7['text'] == 'X':
            actu.set("C'est gagné !")
        ia()
        if bouton_c1['text'] == 'O' and bouton_c2['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c4['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c6['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c8['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c4['text'] == 'O' and bouton_c7['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c2['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c8['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c9['text'] == 'O' and bouton_c6['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
    else:
        actj.set("Cette emplacement est déjà pris !")

def c6():
    if bouton_c6['text'] == '':
        bouton_c6['fg'] = 'blue'
        bouton_c6['text'] = 'X'
        if bouton_c5['text'] == 'X' and bouton_c4['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c9['text'] == 'X' and bouton_c3['text'] == 'X':
            actu.set("C'est gagné !")
        ia()
        if bouton_c1['text'] == 'O' and bouton_c2['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c4['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c6['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c8['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c4['text'] == 'O' and bouton_c7['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c2['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c8['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c9['text'] == 'O' and bouton_c6['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
    else:
        actj.set("Cette emplacement est déjà pris !")

def c7():
    if bouton_c7['text'] == '':
        bouton_c7['fg'] = 'blue'
        bouton_c7['text'] = 'X'
        if bouton_c4['text'] == 'X' and bouton_c1['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c5['text'] == 'X' and bouton_c3['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c8['text'] == 'X' and bouton_c9['text'] == 'X':
            actu.set("C'est gagné !")
        ia()
        if bouton_c1['text'] == 'O' and bouton_c2['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c4['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c6['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c8['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c4['text'] == 'O' and bouton_c7['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c2['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c8['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c9['text'] == 'O' and bouton_c6['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
    else:
        actj.set("Cette emplacement est déjà pris !")

def c8():
    if bouton_c8['text'] == '':
        bouton_c8['fg'] = 'blue'
        bouton_c8['text'] = 'X'
        if bouton_c7['text'] == 'X' and bouton_c9['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c5['text'] == 'X' and bouton_c2['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c9['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c1['text'] == 'X' and bouton_c3['text'] == '':
            bouton_c3['text'] = 'O'
        else:
            ia()
        if bouton_c1['text'] == 'O' and bouton_c2['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c4['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c6['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c8['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c4['text'] == 'O' and bouton_c7['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c2['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c8['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c9['text'] == 'O' and bouton_c6['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
    else:
        actj.set("Cette emplacement est déjà pris !")

def c9():
    if bouton_c9['text'] == '':
        bouton_c9['fg'] = 'blue'
        bouton_c9['text'] = 'X'
        if bouton_c5['text'] == 'X' and bouton_c1['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c6['text'] =='X' and bouton_c3['text'] == 'X':
            actu.set("C'est gagné !")
        if bouton_c8['text'] == 'X' and bouton_c7['text'] == 'X':
            actu.set("C'est gagné !")
        ia()
        if bouton_c1['text'] == 'O' and bouton_c2['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c4['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c6['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c8['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c4['text'] == 'O' and bouton_c7['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c2['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c8['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c9['text'] == 'O' and bouton_c6['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c1['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c9['text'] == 'O':
            actu.set("C'est perdu !")
        if bouton_c7['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c3['text'] == 'O':
            actu.set("C'est perdu !")
    else:
        actj.set("Cette emplacement est déjà pris !")

def ia():
    if bouton_c8['text'] == 'O' and bouton_c7['text'] == 'O' and bouton_c9['text'] == '':
        bouton_c9['text'] = 'O'
    elif bouton_c2['text'] == 'X' and bouton_c5['text'] == 'O' and bouton_c4['text'] == '':
        bouton_c4['text'] = 'O'
    elif bouton_c5['text'] == 'O' and bouton_c4['text'] == 'X' and bouton_c7['text'] == '':
        bouton_c7['text'] = 'O'
    elif bouton_c3['text'] == 'X' and bouton_c5['text'] == 'X' and bouton_c9['text'] == '' and bouton_c7['text'] == 'O':
        bouton_c9['text'] = 'O'
    elif bouton_c7['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c3['text'] == '':
        bouton_c3['text'] = 'O'
    elif bouton_c9['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c1['text'] == '':
        bouton_c1['text'] = 'O'
    elif bouton_c7['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c3['text'] == '':
        bouton_c3['text'] = 'O'
    elif bouton_c1['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c9['text'] == '':
        bouton_c9['text'] = 'O'
    elif bouton_c4['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c6['text'] == '':
        bouton_c6['text'] = 'O'
    elif bouton_c1['text'] == 'O' and bouton_c2['text'] == 'O' and bouton_c3['text'] == '':
        bouton_c3['text'] = 'O'
    elif bouton_c3['text'] == 'O' and bouton_c6['text'] == 'O' and bouton_c9['text'] == '':
        bouton_c9['text'] = 'O'
    elif bouton_c2['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c8['text'] == '':
        bouton_c8['text'] = 'O'
    elif bouton_c1['text'] == 'O' and bouton_c4['text'] == 'O' and bouton_c7['text'] == '':
        bouton_c7['text'] = 'O'
    elif bouton_c7['text'] == 'O' and bouton_c9['text'] == 'O' and bouton_c8['text'] == '':
        bouton_c8['text'] = 'O'
    elif bouton_c4['text'] == 'O' and bouton_c6['text'] == 'O' and bouton_c5['text'] == '':
        bouton_c5['text'] = 'O'
    elif bouton_c1['text'] == 'O' and bouton_c3['text'] == 'O' and bouton_c2['text'] == '':
        bouton_c2['text'] = 'O'
    elif bouton_c3['text'] == 'O' and bouton_c9['text'] == 'O' and bouton_c6['text'] == '':
        bouton_c6['text'] = 'O'
    elif bouton_c2['text'] == 'O' and bouton_c8['text'] == 'O' and bouton_c5['text'] == '':
        bouton_c5['text'] = 'O'
    elif bouton_c1['text'] == 'O' and bouton_c7['text'] == 'O' and bouton_c4['text'] == '':
        bouton_c4['text'] = 'O'
    elif bouton_c8['text'] == 'O' and bouton_c9['text'] == 'O' and bouton_c7['text'] == '':
        bouton_c7['text'] = 'O'
    elif bouton_c6['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c4['text'] == '':
        bouton_c4['text'] = 'O'
    elif bouton_c3['text'] == 'O' and bouton_c2['text'] == 'O' and bouton_c1['text'] == '':
        bouton_c1['text'] = 'O'
    elif bouton_c9['text'] == 'O' and bouton_c6['text'] == 'O' and bouton_c3['text'] == '':
        bouton_c3['text'] = 'O'
    elif bouton_c8['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c2['text'] == '':
        bouton_c2['text'] = 'O'
    elif bouton_c7['text'] == 'O' and bouton_c4['text'] == 'O' and bouton_c1['text'] == '':
        bouton_c1['text'] = 'O'
    elif bouton_c1['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c9['text'] == '':
        bouton_c9['text'] = 'O'
    elif bouton_c9['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c1['text'] == '':
        bouton_c1['text'] = 'O'
    elif bouton_c9['text'] == 'O' and bouton_c1['text'] == 'O' and bouton_c5['text'] == '':
        bouton_c5['text'] = 'O'
    elif bouton_c7['text'] == 'O' and bouton_c3['text'] == 'O' and bouton_c5['text'] == '':
        bouton_c5['text'] = 'O'
    elif bouton_c7['text'] == 'O' and bouton_c5['text'] == 'O' and bouton_c3['text'] == '':
        bouton_c3['text'] = 'O'
    elif bouton_c5['text'] == 'O' and bouton_c3['text'] == 'O' and bouton_c7['text'] == '':
        bouton_c7['text'] = 'O'
    elif bouton_c8['text'] == 'X' and bouton_c7['text'] == 'X' and bouton_c9['text'] == '':
        bouton_c9['text'] = 'O'
    elif bouton_c4['text'] == 'X' and bouton_c5['text'] == 'X' and bouton_c6['text'] == '':
        bouton_c6['text'] = 'O'
    elif bouton_c1['text'] == 'X' and bouton_c2['text'] == 'X' and bouton_c3['text'] == '':
        bouton_c3['text'] = 'O'
    elif bouton_c3['text'] == 'X' and bouton_c6['text'] == 'X' and bouton_c9['text'] == '':
        bouton_c9['text'] = 'O'
    elif bouton_c2['text'] == 'X' and bouton_c5['text'] == 'X' and bouton_c8['text'] == '':
        bouton_c8['text'] = 'O'
    elif bouton_c1['text'] == 'X' and bouton_c4['text'] == 'X' and bouton_c7['text'] == '':
        bouton_c7['text'] = 'O'
    elif bouton_c7['text'] == 'X' and bouton_c9['text'] == 'X' and bouton_c8['text'] == '':
        bouton_c8['text'] = 'O'
    elif bouton_c4['text'] == 'X' and bouton_c6['text'] == 'X' and bouton_c5['text'] == '':
        bouton_c5['text'] = 'O'
    elif bouton_c1['text'] == 'X' and bouton_c3['text'] == 'X' and bouton_c2['text'] == '':
        bouton_c2['text'] = 'O'
    elif bouton_c3['text'] == 'X' and bouton_c9['text'] == 'X' and bouton_c6['text'] == '':
        bouton_c6['text'] = 'O'
    elif bouton_c2['text'] == 'X' and bouton_c8['text'] == 'X' and bouton_c5['text'] == '':
        bouton_c5['text'] = 'O'
    elif bouton_c1['text'] == 'X' and bouton_c7['text'] == 'X' and bouton_c4['text'] == '':
        bouton_c4['text'] = 'O'
    elif bouton_c8['text'] == 'X' and bouton_c9['text'] == 'X' and bouton_c7['text'] == '':
        bouton_c7['text'] = 'O'
    elif bouton_c6['text'] == 'X' and bouton_c5['text'] == 'X' and bouton_c4['text'] == '':
        bouton_c4['text'] = 'O'
    elif bouton_c3['text'] == 'X' and bouton_c2['text'] == 'X' and bouton_c1['text'] == '':
        bouton_c1['text'] = 'O'
    elif bouton_c9['text'] == 'X' and bouton_c6['text'] == 'X' and bouton_c3['text'] == '':
        bouton_c3['text'] = 'O'
    elif bouton_c8['text'] == 'X' and bouton_c5['text'] == 'X' and bouton_c2['text'] == '':
        bouton_c2['text'] = 'O'
    elif bouton_c7['text'] == 'X' and bouton_c4['text'] == 'X' and bouton_c1['text'] == '':
        bouton_c1['text'] = 'O'
    elif bouton_c1['text'] == 'X' and bouton_c5['text'] == 'X' and bouton_c9['text'] == '':
        bouton_c9['text'] = 'O'
    elif bouton_c9['text'] == 'X' and bouton_c5['text'] == 'X' and bouton_c1['text'] == '':
        bouton_c1['text'] = 'O'
    elif bouton_c9['text'] == 'X' and bouton_c1['text'] == 'X' and bouton_c5['text'] == '':
        bouton_c5['text'] = 'O'
    elif bouton_c7['text'] == 'X' and bouton_c3['text'] == 'X' and bouton_c5['text'] == '':
        bouton_c5['text'] = 'O'
    elif bouton_c7['text'] == 'X' and bouton_c5['text'] == 'X' and bouton_c3['text'] == '':
        bouton_c3['text'] = 'O'
    elif bouton_c5['text'] == 'X' and bouton_c3['text'] == 'X' and bouton_c7['text'] == '':
        bouton_c7['text'] = 'O'
    else:
        if bouton_c5['text'] == 'X' and bouton_c9['text'] == 'X' and bouton_c3['text'] == '':
            bouton_c3['text'] = 'O'
        elif bouton_c3['text'] == 'X' or bouton_c9['text'] == 'X' or bouton_c7['text'] == 'X' or bouton_c1['text'] == 'X' and bouton_c5['text'] == '':
            bouton_c5['text'] = 'O'
        elif bouton_c5['text'] == 'X' and bouton_c7['text'] == '':
            bouton_c7['text'] = 'O'
        elif bouton_c5['text'] == 'X' and bouton_c8['text'] == '':
            bouton_c8['text'] = 'O'
        elif bouton_c5['text'] == 'X' and bouton_c9['text'] == '':
            bouton_c9['text'] = 'O'
        elif bouton_c5['text'] == 'X' and bouton_c6['text'] == '':
            bouton_c6['text'] = 'O'
        elif bouton_c5['text'] == 'X' and bouton_c3['text'] == '':
            bouton_c3['text'] = 'O'
        elif bouton_c5['text'] == 'X' and bouton_c2['text'] == '':
            bouton_c2['text'] = 'O'
        elif bouton_c5['text'] == 'X' and bouton_c1['text'] == '':
            bouton_c1['text'] = 'O'
        elif bouton_c5['text'] == 'X' and bouton_c4['text'] == '':
            bouton_c4['text'] = 'O'
        elif bouton_c4['text'] == 'X' and bouton_c7['text'] == '':
            bouton_c7['text'] = 'O'
        elif bouton_c4['text'] == 'X' and bouton_c5['text'] == '':
            bouton_c5['text'] = 'O'
        elif bouton_c4['text'] == 'X' and bouton_c1['text'] == '':
            bouton_c1['text'] = 'O'
        elif bouton_c4['text'] == 'X' and bouton_c2['text'] == '':
            bouton_c2['text'] = 'O'
        elif bouton_c4['text'] == 'X' and bouton_c8['text'] == '':
            bouton_c8['text'] = 'O'
        elif bouton_c4['text'] == 'X' and bouton_c6['text'] == '':
            bouton_c6['text'] = 'O'
        elif bouton_c4['text'] == 'X' and bouton_c9['text'] == '':
            bouton_c9['text'] = 'O'
        elif bouton_c4['text'] == 'X' and bouton_c3['text'] == '':
            bouton_c3['text'] = 'O'
        elif bouton_c6['text'] == 'X' and bouton_c9['text'] == '':
            bouton_c9['text'] = 'O'
        elif bouton_c6['text'] == 'X' and bouton_c3['text'] == '':
            bouton_c3['text'] = 'O'
        elif bouton_c6['text'] == 'X' and bouton_c5['text'] == '':
            bouton_c5['text'] = 'O'
        elif bouton_c6['text'] == 'X' and bouton_c2['text'] == '':
            bouton_c2['text'] = 'O'
        elif bouton_c6['text'] == 'X' and bouton_c8['text'] == '':
            bouton_c8['text'] = 'O'
        elif bouton_c6['text'] == 'X' and bouton_c4['text'] == '':
            bouton_c4['text'] = 'O'
        elif bouton_c6['text'] == 'X' and bouton_c7['text'] == '':
            bouton_c7['text'] = 'O'
        elif bouton_c6['text'] == 'X' and bouton_c1['text'] == '':
            bouton_c1['text'] = 'O'
        elif bouton_c1['text'] == 'X' and bouton_c9['text'] == '':
            bouton_c9['text'] = 'O'
        elif bouton_c1['text'] == 'X' and bouton_c2['text'] == '':
            bouton_c2['text'] = 'O'
        elif bouton_c1['text'] == 'X' and bouton_c4['text'] == '':
            bouton_c4['text'] = 'O'
        elif bouton_c1['text'] == 'X' and bouton_c5['text'] == '':
            bouton_c5['text'] = 'O'
        elif bouton_c1['text'] == 'X' and bouton_c7['text'] == '':
            bouton_c7['text'] = 'O'
        elif bouton_c1['text'] == 'X' and bouton_c3['text'] == '':
            bouton_c3['text'] = 'O'
        elif bouton_c1['text'] == 'X' and bouton_c8['text'] == '':
            bouton_c8['text'] = 'O'
        elif bouton_c1['text'] == 'X' and bouton_c6['text'] == '':
            bouton_c6['text'] = 'O'
        elif bouton_c2['text'] == 'X' and bouton_c1['text'] == '':
            bouton_c1['text'] = 'O'
        elif bouton_c2['text'] == 'X' and bouton_c3['text'] == '':
            bouton_c3['text'] = 'O'
        elif bouton_c2['text'] == 'X' and bouton_c5['text'] == '':
            bouton_c5['text'] = 'O'
        elif bouton_c2['text'] == 'X' and bouton_c4['text'] == '':
            bouton_c4['text'] = 'O'
        elif bouton_c2['text'] == 'X' and bouton_c6['text'] == '':
            bouton_c6['text'] = 'O'
        elif bouton_c2['text'] == 'X' and bouton_c8['text'] == '':
            bouton_c8['text'] = 'O'
        elif bouton_c2['text'] == 'X' and bouton_c7['text'] == '':
            bouton_c7['text'] = 'O'
        elif bouton_c2['text'] == 'X' and bouton_c9['text'] == '':
            bouton_c9['text'] = 'O'
        elif bouton_c3['text'] == 'X' and bouton_c7['text'] == '':
            bouton_c7['text'] = 'O'
        elif bouton_c3['text'] == 'X' and bouton_c2['text'] == '':
            bouton_c2['text'] = 'O'
        elif bouton_c3['text'] == 'X' and bouton_c6['text'] == '':
            bouton_c6['text'] = 'O'
        elif bouton_c3['text'] == 'X' and bouton_c5['text'] == '':
            bouton_c5['text'] = 'O'
        elif bouton_c3['text'] == 'X' and bouton_c1['text'] == '':
            bouton_c1['text'] = 'O'
        elif bouton_c3['text'] == 'X' and bouton_c9['text'] == '':
            bouton_c9['text'] = 'O'
        elif bouton_c3['text'] == 'X' and bouton_c4['text'] == '':
            bouton_c4['text'] = 'O'
        elif bouton_c3['text'] == 'X' and bouton_c8['text'] == '':
            bouton_c8['text'] = 'O'
        elif bouton_c7['text'] == 'X' and bouton_c3['text'] == '':
            bouton_c3['text'] = 'O'
        elif bouton_c7['text'] == 'X' and bouton_c4['text'] == '':
            bouton_c4['text'] = 'O'
        elif bouton_c7['text'] == 'X' and bouton_c8['text'] == '':
            bouton_c8['text'] = 'O'
        elif bouton_c7['text'] == 'X' and bouton_c5['text'] == '':
            bouton_c5['text'] = 'O'
        elif bouton_c7['text'] == 'X' and bouton_c1['text'] == '':
            bouton_c1['text'] = 'O'
        elif bouton_c7['text'] == 'X' and bouton_c9['text'] == '':
            bouton_c9['text'] = 'O'
        elif bouton_c7['text'] == 'X' and bouton_c2['text'] == '':
            bouton_c2['text'] = 'O'
        elif bouton_c7['text'] == 'X' and bouton_c6['text'] == '':
            bouton_c6['text'] = 'O'
        elif bouton_c8['text'] == 'X' and bouton_c5['text'] == '':
            bouton_c5['text'] = 'O'
        elif bouton_c8['text'] == 'X' and bouton_c7['text'] == '':
            bouton_c7['text'] = 'O'
        elif bouton_c8['text'] == 'X' and bouton_c9['text'] == '':
            bouton_c9['text'] = 'O'
        elif bouton_c8['text'] == 'X' and bouton_c4['text'] == '':
            bouton_c4['text'] = 'O'
        elif bouton_c8['text'] == 'X' and bouton_c6['text'] == '':
            bouton_c6['text'] = 'O'
        elif bouton_c8['text'] == 'X' and bouton_c2['text'] == '':
            bouton_c2['text'] = 'O'
        elif bouton_c8['text'] == 'X' and bouton_c1['text'] == '':
            bouton_c1['text'] = 'O'
        elif bouton_c8['text'] == 'X' and bouton_c3['text'] == '':
            bouton_c3['text'] = 'O'
        elif bouton_c9['text'] == 'X' and bouton_c1['text'] == '':
            bouton_c1['text'] = 'O'
        elif bouton_c9['text'] == 'X' and bouton_c8['text'] == '':
            bouton_c8['text'] = 'O'
        elif bouton_c9['text'] == 'X' and bouton_c6['text'] == '':
            bouton_c6['text'] = 'O'
        elif bouton_c9['text'] == 'X' and bouton_c5['text'] == '':
            bouton_c5['text'] = 'O'
        elif bouton_c9['text'] == 'X' and bouton_c7['text'] == '':
            bouton_c7['text'] = 'O'
        elif bouton_c9['text'] == 'X' and bouton_c3['text'] == '':
            bouton_c3['text'] = 'O'
        elif bouton_c9['text'] == 'X' and bouton_c4['text'] == '':
            bouton_c4['text'] = 'O'

def rejouer():
    bouton_c1['fg'] = 'red'
    bouton_c2['fg'] = 'red'
    bouton_c3['fg'] = 'red'
    bouton_c4['fg'] = 'red'
    bouton_c5['fg'] = 'red'
    bouton_c6['fg'] = 'red'
    bouton_c7['fg'] = 'red'
    bouton_c8['fg'] = 'red'
    bouton_c9['fg'] = 'red'
    bouton_c1['text'] = ''
    bouton_c2['text'] = ''
    bouton_c3['text'] = ''
    bouton_c4['text'] = ''
    bouton_c5['text'] = ''
    bouton_c6['text'] = ''
    bouton_c7['text'] = ''
    bouton_c8['text'] = ''
    bouton_c9['text'] = ''
    actj.set("")
    actu.set("")

###PROGRAMME PRINCIPAL###

bg=Label(fenetre,
            relief=FLAT, fg="white", bg="grey9", width=66, height=30)
bg.place(x=530, y=195)
titre = Label(fenetre, text="MORPIONS", relief=FLAT, fg="white", bg="grey7", width=22, height=1, font=("Courier", 30))
titre.place(x=500, y=30)

bouton_reinit = Button(fenetre, text="Quitter", width=5, bg="grey7", fg="red", command=quitter, relief=FLAT, activebackground='red')
# On crée le bouton pour quitter
bouton_reinit.place(x=10, y=10)
bouton_c1 = Button(fenetre, text="", height=9, width=20, bg="grey7", fg="red", command=c1, relief=FLAT, activebackground='grey8')
# On crée la case en haut à gauche
bouton_c1.place(x=535, y=200)
bouton_c2 = Button(fenetre, text="", height=9, width=20, bg="grey7", fg="red", command=c2, relief=FLAT, activebackground='grey8')
# On crée la case en haut
bouton_c2.place(x=690, y=200)
bouton_c3 = Button(fenetre, text="", height=9, width=20, bg="grey7", fg="red", command=c3, relief=FLAT, activebackground='grey8')
# On crée la case en haut à droite
bouton_c3.place(x=845, y=200)
bouton_c4 = Button(fenetre, text="", height=9, width=20, bg="grey7", fg="red", command=c4, relief=FLAT, activebackground='grey8')
# On crée la case à gauche
bouton_c4.place(x=535, y=350)
bouton_c5 = Button(fenetre, text="", height=9, width=20, bg="grey7", fg="red", command=c5, relief=FLAT, activebackground='grey8')
# On crée la case au milieu
bouton_c5.place(x=690, y=350)
bouton_c6 = Button(fenetre, text="", height=9, width=20, bg="grey7", fg="red", command=c6, relief=FLAT, activebackground='grey8')
# On crée la case à droite
bouton_c6.place(x=845, y=350)
bouton_c7 = Button(fenetre, text="", height=9, width=20, bg="grey7", fg="red", command=c7, relief=FLAT, activebackground='grey8')
# On crée la case en bas à gauche
bouton_c7.place(x=535, y=500)
bouton_c8 = Button(fenetre, text="", height=9, width=20, bg="grey7", fg="red", command=c8, relief=FLAT, activebackground='grey8')
# On crée la case en bas
bouton_c8.place(x=690, y=500)
bouton_c9 = Button(fenetre, text="", height=9, width=20, bg="grey7", fg="red", command=c9, relief=FLAT, activebackground='grey8')
# On crée la case en bas à droite
bouton_c9.place(x=845, y=500)
bouton_r = Button(fenetre, text="Rejouer", width=15, height=2, bg="grey7", fg="spring green", command=rejouer, relief=FLAT, activebackground='grey8')
# On crée le bouton pour relancer une partie
bouton_r.place(x=1050, y=400)

actj = StringVar()
actjrep = Label(fenetre, textvariable=actj, fg='spring green', bg='#1b1b1b', font=("Fixedsys"))
actjrep.place(x=150, y=240)
actj.set("")

actu = StringVar()
acturep = Label(fenetre, textvariable=actu, fg='spring green', bg='#1b1b1b', font=("Fixedsys"))
acturep.place(x=150, y=280)
actu.set("")


fenetre.mainloop()
# Exécution de la fenêtre