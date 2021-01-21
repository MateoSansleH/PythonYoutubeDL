from librairie import biblio
import urllib.request
import re
from pytube import *
from ping3 import ping, verbose_ping
import moviepy.editor
import os

def affichage_liste_video(liste_liens_video):
    titre_video = ["Titre ",]
    auteur_video = ["Chaine Youtube ",]
    duree_video = ["Durée ",]

#creation de 3 listes
    for i in range(0, 5):
        titre_video.append(YouTube(liste_liens_video[i]).title)
        auteur_video.append(YouTube(liste_liens_video[i]).author)
        duree_video.append(YouTube(liste_liens_video[i]).length)

    titre_video.append("ANNULE")
    auteur_video.append("")
    duree_video.append("")

    longueur_titre_video = -1
    i= 0
    while i < len(titre_video):
        if len(titre_video[i]) > longueur_titre_video:
            longueur_titre_video = len(titre_video[i])
        i += 1

    longueur_auteur_video = -1
    i= 0
    while i < len(auteur_video):
        if len(auteur_video[i]) > longueur_auteur_video:
            longueur_auteur_video = len(auteur_video[i])
        i += 1

    longueur_duree_video = -1
    i= 0
    while i < len(duree_video):
        if len(str(duree_video[i])) > longueur_duree_video:
            longueur_duree_video = len(str(duree_video[i]))
        i += 1
    #print(longueur_titre_video)
    #print(longueur_auteur_video)
    #print(longueur_duree_video)

    i = 0
    while i < len(titre_video):
        if len(titre_video[i]) < longueur_titre_video:
            for y in range(len(titre_video[i]), longueur_titre_video):
                titre_video[i] = titre_video[i] + " "
        i += 1

    i = 0
    while i < len(auteur_video):
        if len(auteur_video[i]) < longueur_auteur_video:
            for y in range(len(auteur_video[i]), longueur_auteur_video):
                auteur_video[i] = auteur_video[i] + " "
        i += 1

    i = 0
    while i < len(duree_video):
        if len(str(duree_video[i])) < longueur_duree_video:
            for y in range(len(str(duree_video[i])), longueur_duree_video):
                duree_video[i] = str(duree_video[i]) + " "
        i += 1

    longeur_total_tableau = longueur_titre_video + longueur_auteur_video + longueur_duree_video
    correction = 10
    print("#" + (longeur_total_tableau + correction) * "=" + "#")
    i = 0
    print("# " + str(titre_video[i]) + 2*" " + " # " + str(auteur_video[i]) + " # " + str(duree_video[i]) + " # ")
    print("#" + (longeur_total_tableau + correction) * "=" + "#")
    i = 1
    while i < 6:
        print("#[" + str(i) + "]" + str(titre_video[i]) + " # " + str(auteur_video[i]) + " # " + str(duree_video[i]) + " # ")
        i += 1
    print("#[0]" + str(titre_video[i]) + " # " + str(auteur_video[i]) + " # " + str(duree_video[i]) + " # ")
    print("#" + (longeur_total_tableau + correction) * "=" + "#")