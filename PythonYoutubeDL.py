from librairie import biblio, tableau
import urllib.request
import re
from pytube import *
from ping3 import ping, verbose_ping
import moviepy.editor
import os
import time

def listevideo(url_recherche):
    page_web = urllib.request.urlopen(url_recherche)
    liste_identifiant_video = re.findall(r"watch\?v=(\S{11})", page_web.read().decode())
    liste_liens_video = []
    for i in liste_identifiant_video:
        liste_liens_video.append("https://www.youtube.com/watch?v=" + i)
    return liste_liens_video

def downloadvideo(listeurl, numero_video):
    video = YouTube(listeurl[numero_video]).streams.get_highest_resolution()
    video.download("output/tmp", "video1")


def main():
    biblio.bonjour()
    host = "www.youtube.com"
    #host="pas d'internet"
    sortie = biblio.internetconnection(host)
    time.sleep(1.25)
    ## Boucle pour telecharger plusieurs musiques
    while sortie != 1 :
        #Debut du programme
        print("")
        print("Veuillez entrer votre recherche :")
        recherche = biblio.demande() #recherche du la musique
        #print(recherche)

        recherche = biblio.spacetoplus(recherche)    #converison de la recherche
        #print(recherche)

        os.system("cls")
        
        url_recherche = "https://www.youtube.com/results?search_query="+ recherche
        #print(url_recherche)
        
        liste_liens_video = listevideo(url_recherche)
        #print(liste_liens_video)

        print("please wait ...")
        tableau.affichage_liste_video(liste_liens_video)
        print("Veuillez choisir la video a télecharger :")
        choix_video = biblio.choixde1a5()
        #print(choix_video)

        

        if choix_video != -1:
            downloadvideo(liste_liens_video, choix_video)
            titre_video = YouTube(liste_liens_video[choix_video]).title
            #titre_video = biblio.replacespace(YouTube(liste_liens_video[choix_video]).title, "_")
            titre_video = biblio.cleantitle(titre_video)
            biblio.splitaudiovideo("output/tmp/video1.mp4", "output/" +  titre_video + ".mp3")

        os.system("cls")
        sortie = biblio.quitprgm() ## Focntion de fin de boucle
        os.system("cls")
        
if __name__ == '__main__':
    main()
